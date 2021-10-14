import sys
from antlr4 import *
from antlr4.tree.Trees import TerminalNode
from antlr4.error.Errors import *
from DecafLexer import DecafLexer
from DecafParser import DecafParser
from DecafListener import DecafListener

class VarSymbolTableItem():
    """
    varId: variables name.
    varType: variable type.
    num: if its a singular value or if it contains more, meaning its an array.
    varContext: parameter or a normal variable.
    size: size of the variable depending on its type.
    offset: memory offset

    scope: scope it belongs to. (CURRENTLY OMMITED)
    """
    def __init__(self, varId, varType, varContext, num, size, isArray, offset, scope):
        self.varId = varId 
        self.varType = varType
        self.value = None
        self.num = num
        self.size = size
        self.offset = offset
        self.varContext = varContext
        self.isArray = isArray
        self.scope = scope

class StructSymbolTableItem():
    def __init__(self, structId, structMembers):
        self.structId = structId
        self.structMembers = structMembers
        self.size = 0

class SymbolTableItem():
    def __init__(self, parentKey, symbolTable, returnType):
        self.parentKey = parentKey
        self.returnType = returnType
        self.symbolTable = symbolTable

"""
Represents a Quad to be stored in a list.

Kind of literal to the book in everything.
    op: stores an internal code for the operator. Sometimes implicit. i.e. assignment operation.
    arg1: stores arg1, every Quad will have an arg1.
    arg2: stores arg2, not every operation will need to use arg2. i.e. minus or not operations.
    result: stores the result of the operation. Some operators dont use this
"""
class QuadBucket():
    def __init__(self, op, arg1, arg2, result):
        # String
        self.op = op
        # AddrEntry
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

class AddrEntry():
    def __init__(self, addr, lblTrue, lblFalse, lblNext):
        self.addr = addr
        self.lblTrue = lblTrue
        self.lblFalse = lblFalse
        self.lblNext = lblNext

#---------------------------------------------------------------------------------------------------

class DecafPrinter(DecafListener):
    def __init__(self) -> None:
        # Flags or misc
        self.errorDictionary = {}
        self.primitives = ('int', 'char', 'boolean', 'struct', 'void')
        self.typeSizes = {'int':4, 'char':1, 'boolean':1}
        self.nodeTypes = {}
        self.mainFound = False
        self.structToUse = None
        self.structStack = []

        # Symbol table related
        self.localOffset = 0
        self.globalOffset = 0
        self.structOffset = 0

        self.currentMethodName = ""
        self.currentScope = "global"
        self.pastScope = "None"
        self.nestedCounter = 1
        self.scopeDictionary = {}
        self.structDictionary = {}

        # Intermediate code generation
        self.quadList = []
        self.nodeAddr = {}
        self.tempCounter = 1
        self.blockCounter = 1
        self.loopCounter = 1
        self.relCounter = 1
        self.firstCheck = False
        self.currentStructMovement = 0
        self.arrayInfo = []

        self.addScopeToSymbolTable(None)
        super().__init__()

    def returnErrorList(self):
        return self.errorList

    # -----------------------------------------------------------------------
    # Listener override methods
    def enterVarDeclaration(self, ctx: DecafParser.VarDeclarationContext):
        value = None
        isArray = False
        if (ctx.NUM() != None):
            value = ctx.getChild(3).getText()
            isArray = True

            if (int(value) <= 0):
                self.nodeTypes[ctx] = 'error'
                self.addError((ctx.start.line, "arrayError"), "Array size must be bigger than 0")
                return

        parentCtx = ctx.parentCtx
        firstChild = parentCtx.getChild(0).getText()

        varType = ctx.getChild(0).getText()
        varId = ctx.getChild(1).getText()

        if firstChild == "struct":
            structId = parentCtx.getChild(1).getText()
            added = self.addVarToStruct(structId, varType, varId, "blockVar", value, isArray, self.currentScope)

            if (added):
                self.nodeTypes[ctx] = 'void'
            else:
                self.nodeTypes[ctx] = 'error'
                errorMsg = "Failed to add variable " + varId + " to struct, variable already exists."
                self.addError((ctx.start.line, "existingValue"), errorMsg)
        else:
            added = self.addVarToSymbolTable(varType, varId, "blockVar", value, isArray, self.currentScope)

            if (added):
                self.nodeTypes[ctx] = 'void'
            else:
                self.nodeTypes[ctx] = 'error'
                errorMsg = "Failed to add variable " + varId + " to scope, variable already exists."
                self.addError((ctx.start.line, "existingValue"), errorMsg)

 
    def enterMethodDeclaration(self, ctx: DecafParser.MethodDeclarationContext):
        methodType = ctx.getChild(0).getText()
        methodName = ctx.getChild(1).getText()

        self.currentMethodName = methodName
        self.enterScope(methodName)

        # Add to symbol table!
        added = self.addScopeToSymbolTable(self.pastScope, methodType)

        if (added):
            self.nodeTypes[ctx] = 'void'

            """ Code generation """
            # Create new label
            newLabel = self.createLabel(methodName)
            newAddr = self.createAddrLiteral(newLabel)
            self.addQuad("label", newAddr, None, None)

        else:
            self.nodeTypes[ctx] = 'error'
            errorMsg = "Failed to add method " + methodName + " to symbol table, there's already a method with that name."
            self.addError((ctx.start.line, "existingMethod"), errorMsg)

    def enterBlock(self, ctx: DecafParser.BlockContext):
        parentCtx = ctx.parentCtx
        firstChild = parentCtx.getChild(0).getText()

        # Normal block
        if firstChild not in self.primitives:
            nestedBlockName = self.currentMethodName + str(self.nestedCounter)
            self.nestedCounter += 1
            self.enterScope(nestedBlockName)
        
        # Add to symbol table!
        added = self.addScopeToSymbolTable(self.pastScope)

        if (added):
            self.nodeTypes[ctx] = 'void'

        """ Code generation """
        # If / Else
        if (type(parentCtx) == DecafParser.Stat_ifContext):
            exprAddr = self.nodeAddr[parentCtx.getChild(2)]
            if (self.firstCheck == False):
                self.addQuad("labelt", exprAddr, None, None)
                self.firstCheck = True 
            else:
                nextAddr = self.nodeAddr[parentCtx.getChild(4)]
                self.addQuad('goton', nextAddr, None, None)
                self.addQuad("labelf", exprAddr, None, None)

        # While
        if (type(parentCtx) == DecafParser.Stat_elseContext):
            exprAddr = self.nodeAddr[parentCtx.getChild(2)]
            
            # Print label true
            self.addQuad('labelt', exprAddr, None, None)

    def enterParameter(self, ctx: DecafParser.ParameterContext):
        isArray = False
        if (len(ctx.children) > 2): isArray=True

        paramType = ctx.getChild(0).getText()

        if paramType != 'void':
            paramId = ctx.getChild(1).getText()

            added = self.addVarToSymbolTable(paramType, paramId, "param", None, isArray, self.currentScope)
            if (added):
                self.nodeTypes[ctx] = 'void'
            else:
                self.nodeTypes[ctx] = 'error'
                errorMsg = "Failed to add parameter " + paramId + " to symbol table, there's already an existing parameter with that name."
                self.addError((ctx.start.line, "existingValue"), errorMsg)

    def enterStructDeclaration(self, ctx: DecafParser.StructDeclarationContext):
        structId = ctx.getChild(1).getText()
        self.addStructToSymbolTable(structId)

    def enterLocation(self, ctx: DecafParser.LocationContext):
        if (ctx.location()):
            varId = ctx.getChild(0).getText()

            if (self.structStack == []):
                structVarType = self.lookupVarInSymbolTable(varId, self.currentScope)
                structToUse = self.searchStructMember(structVarType.varType)
                self.structStack.append(structToUse)
            else:
                structVarType = self.structStack[-1].structMembers[varId]
                structToUse = self.searchStructMember(structVarType.varType)
                self.structStack.append(structToUse)

    def enterStat_if(self, ctx: DecafParser.Stat_ifContext):
        labelTrue = self.createLabel("block"+str(self.blockCounter)+".true")
        labelNext = self.createLabel("s"+str(self.blockCounter)+".next")

        nextAddr = self.createAddrNext(labelNext)

        # Else
        if (len(ctx.children) > 5):
            labelFalse = self.createLabel("block"+str(self.blockCounter)+".false")
            exprAddr = self.createAddrLabels(labelTrue, labelFalse)
        else:
            labelFalse = labelNext
            exprAddr = self.createAddrLabels(labelTrue, labelFalse)

        self.nodeAddr[ctx.getChild(2)] = exprAddr
        self.nodeAddr[ctx.getChild(4)] = nextAddr

    # While but it's wrongly named
    def enterStat_else(self, ctx: DecafParser.Stat_elseContext):
        labelBegin = self.createLabel("loop"+str(self.loopCounter)+".begin")

        labelTrue = self.createLabel("block"+str(self.blockCounter)+".true")
        labelFalse = self.createLabel("s"+str(self.blockCounter)+".next")

        #self.nodeAddr[ctx] = self.createAddrLabels
        self.nodeAddr[ctx.getChild(2)] = self.createAddrLabels(labelTrue, labelFalse)
        self.nodeAddr[ctx.getChild(4)] = self.createAddrNext(labelBegin)

        # Print label(begin)
        self.addQuad('labeln', self.nodeAddr[ctx.getChild(4)], None, None)
        # Can now print expression code

    # Falta generacion de codigo
    # ||
    def enterExpr_arith1(self, ctx: DecafParser.Expr_arith1Context):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)

        op1False = self.createLabel("rel"+str(self.relCounter)+".false")

        self.nodeAddr[op1] = self.createAddrLabels(self.nodeAddr[ctx].lblTrue, op1False)
        self.nodeAddr[op2] = self.nodeAddr[ctx]

    # &&
    def enterExpr_arith2(self, ctx: DecafParser.Expr_arith2Context):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)

        op1True = self.createLabel("rel"+str(self.relCounter)+".true")

        self.nodeAddr[op1] = self.createAddrLabels(op1True, self.nodeAddr[ctx].lblFalse)
        self.nodeAddr[op2] = self.nodeAddr[ctx]

    # !
    def enterExpr_not(self, ctx: DecafParser.Expr_notContext):
        op = ctx.getChild(1)

        self.nodeAddr[op] = self.nodeAddr[ctx]

    # ----------------------------------------------------------------------
    # Exit
    """ General purpose """
    def exitStructDeclaration(self, ctx: DecafParser.StructDeclarationContext):
        self.structOffset = 0

    def exitMethodDeclaration(self, ctx: DecafParser.MethodDeclarationContext):
        methodName = ctx.getChild(1).getText()
        if (methodName == 'main'):
            self.mainFound = True

        self.nestedCounter = 1
        self.tempCounter = 1
        self.localOffset = 0
        self.currentMethodName = "global"

        self.enterScope("global")

    def exitBlock(self, ctx: DecafParser.BlockContext):
        currentBlockObj = self.lookupMethodInSymbolTable(self.currentScope)
        self.enterScope(currentBlockObj.parentKey)

    def exitMethodCall(self, ctx: DecafParser.MethodCallContext):
        #self.nodeTypes[ctx] = self.nodeTypes[ctx.getChild(0)]
        methodName = ctx.getChild(0).getText()
        args = ctx.getChild(2).getText()

        methodObj = self.lookupMethodInSymbolTable(methodName)

        if (methodObj != None):
            methodCallTypes = []

            for i in range(0, len(ctx.children)):
                if i > 1 and i < len(ctx.children)-1:
                    if (ctx.getChild(i).getText() != ","):
                        methodCallTypes.append(self.nodeTypes[ctx.getChild(i)])

            paramsEquality = self.compareParameters(methodObj, args, methodCallTypes)

            if paramsEquality:
                self.nodeTypes[ctx] = methodObj.returnType

                """ Code generation """
                # Param calls
                for i in range(0, len(ctx.children)):
                    if i > 1 and i < len(ctx.children)-1:
                        if (ctx.getChild(i).getText() != ","):
                            #paramAddr = AddrEntry(ctx.getChild(i).getText(), None, None, None)
                            self.addQuad('param', self.nodeAddr[ctx.getChild(i)], None, None)

                # Function call
                methodAddr = AddrEntry("l_"+methodName+","+str(len(methodCallTypes)), None, None, None)
                self.addQuad('call', methodAddr, None, None)

            else:
                self.nodeTypes[ctx] = 'error'
                self.addError((ctx.start.line, "paramNoMatch"), "Failed to call method, parameters don't match (either in type or order is incorrect)")
        else:
            self.nodeTypes[ctx] = 'error'
            self.addError((ctx.start.line, "noExistingMethod"), "Method doesn't exist in symbol table or hasn't been declared yet.")

    def exitStat_mcall(self, ctx: DecafParser.Stat_mcallContext):
        self.nodeTypes[ctx] = self.nodeTypes[ctx.methodCall()]
        
    def exitProgram(self, ctx: DecafParser.ProgramContext):
        if (not self.mainFound):
            self.nodeTypes[ctx] = 'error'
            self.addError((ctx.start.line, "mainNotFound"), "Main method is not declared!")

    def exitStat_return(self, ctx: DecafParser.StatementContext):
        # Children structure
        # 0: Return
        # 1: Value
        # 2: ;
        # Everything related to returns
        if ctx.getChild(0).getText() == "return":
            rootMethod = self.getRootMethod(self.currentScope)
            methodType = rootMethod.returnType
            expressionOom = ctx.getChild(1)

            if (ctx.getChild(1).getText() == ""):
                if (methodType == 'void'):
                    self.nodeTypes[ctx] = 'void'
                elif(methodType in self.primitives):
                    self.nodeTypes[ctx] = 'error'
                    self.addError((ctx.start.line, "untypedMethod"), "Typed method expecting a return value.")
                else:
                    self.nodeTypes[ctx] = 'error' 
                    self.addError((ctx.start.line, "unacceptedMethodType"), "Method type is not accepted by language.")
            else:
                if (methodType in self.primitives):
                    exprType = self.nodeTypes[expressionOom.getChild(0)]

                    if (exprType == methodType):
                        self.nodeTypes[ctx] = 'void'
                    else:
                        self.nodeTypes[ctx] = 'error'
                        self.addError((ctx.start.line, "returnNotMatching"), "Return statement type doesn't match with method type.")
                else:
                    self.nodeTypes[ctx] = 'error' 
                    self.addError((ctx.start.line, "unacceptedMethodType"), "Method type is not accepted by language.")   

    def exitLocation(self, ctx: DecafParser.LocationContext):
        myvar = None
        calculateStruct = False
        lastChild = False
        isMiddle = False
        # ------------------------------------------------------------------------------------------------------------
        # Syntax check: Structs
        #   Case 1: There is a property being accesed.
        #           ex: a.b.c
        if (ctx.location() != None):
            # Any other struct that is not the root of a struct
            # ex: b in a.b.c
            if self.structStack != []:
                currentTable = self.structStack.pop()
                if (currentTable != None):
                    myvar = currentTable.structMembers[ctx.getChild(0).getText()]
                    if (myvar != None):
                        self.nodeTypes[ctx] = self.nodeTypes[ctx.location()]
                        self.currentStructMovement += myvar.size
                        isMiddle = True
                    else:
                        self.nodeTypes[ctx] = 'error'
                        errorMsg = "Property " + ctx.getChild(0).getText() + " not found on struct."
                        self.addError((ctx.start.line, "propNotFound"), errorMsg)
                else:
                    self.nodeTypes[ctx] = 'error'
                    self.addError((ctx.start.line, "propNoStruct"), "Property is not an struct.")
            # Root of struct
            # ex: a in a.b.c
            else:
                myvar = self.lookupVarInSymbolTable(ctx.getChild(0).getText(), self.currentScope)
                if (myvar != None):
                    #structToUse = self.searchStructMember(structVarType.varType)
                    self.nodeTypes[ctx] = self.nodeTypes[ctx.location()]
                    calculateStruct = True
                else:
                    self.nodeTypes[ctx] = 'error'
                    self.addError((ctx.start.line, "unreachable"), "Undefined.")
        #   Case 2: Property and parent is a struct
        #       ex: c in a.b.c
        elif (type(ctx.parentCtx) == DecafParser.LocationContext and ctx.location() == None):
            if self.structStack != []:
                currentTable = self.structStack.pop()
                if (currentTable != None):
                    myvar = currentTable.structMembers[ctx.getChild(0).getText()]
                    if (myvar != None):                      
                        self.nodeTypes[ctx] = myvar.varType    
                        self.currentStructMovement += myvar.offset
                        lastChild = True 
                        isMiddle = True
                    else:
                        self.nodeTypes[ctx] = 'error'
                        errorMsg = "Property " + ctx.getChild(0).getText() + " not found on struct."
                        self.addError((ctx.start.line, "propNotFound"), errorMsg)                                
                else:
                    self.nodeTypes[ctx] = 'error'
                    self.addError((ctx.start.line, "propNoStruct"), "Parent struct doesn't have this property.")
        # ------------------------------------------------------------------------------------------------------------
        # Syntax check: Normal var. Var that doesn't belong to a struct.
        else:
            myvar = self.lookupVarInSymbolTable(ctx.getChild(0).getText(), self.currentScope)
            if (myvar != None):
                self.nodeTypes[ctx] = myvar.varType

            else:
                self.nodeTypes[ctx] = 'error'
                errorMsgWithVar = "Var " + ctx.getChild(0).getText() + " hasn't been defined yet"
                self.addError((ctx.start.line, "notExistingVar"), errorMsgWithVar)
                return
        # ------------------------------------------------------------------------------------------------------------
        # Syntax check: Array
        if (ctx.expression()):
            if (self.nodeTypes[ctx.expression()] != 'int'):
                self.nodeTypes[ctx] = 'error'
                errorMsg = "<expr> in " + ctx.ID().getText() +  " [<expr>] must be of type int."
                self.addError((ctx.start.line, "arrayError"), errorMsg)  
                return
            if (type(ctx.expression()) == DecafParser.Expr_minusContext):
                self.nodeTypes[ctx] = 'error'
                errorMsg = "Array index of array " +  ctx.ID().getText()  + " must be a non-negative number. "
                self.addError((ctx.start.line, "arrayError"), errorMsg) 
                return
            if (myvar != None):
                if(not myvar.isArray):
                    self.nodeTypes[ctx] = 'error'
                    errorMsgWithVar = "Var " + myvar.varId + " is not an array."
                    self.addError((ctx.start.line, "noArray"), errorMsgWithVar)
                    return
                else:
                    # Var saved and is array
                    if (lastChild): self.arrayInfo = [myvar.varType, ctx.expression()]
        else:
            if (myvar != None):
                if(myvar.isArray):
                    self.nodeTypes[ctx] = 'error'
                    errorMsgWithVar = "Var " + myvar.varId + " is an array. An index should be stated."
                    self.addError((ctx.start.line, "isArray"), errorMsgWithVar)
        # ------------------------------------------------------------------------------------------------------------
        if (myvar != None):
            if (calculateStruct):
                if (self.arrayInfo != []):
                    newTemp = self.getNewTemp()
                    tempAddr = self.createAddrLiteral(newTemp)
                    op1Addr = self.createAddrLiteral(str(self.currentStructMovement))
                    op2Addr = self.createAddrLiteral(str(myvar.offset))
                    self.addQuad('+', op2Addr, op1Addr, tempAddr)

                    arrayTemp = self.getNewTemp()
                    arrayTempAddr = self.createAddrLiteral(arrayTemp)
                    expressionAddr = self.nodeAddr[self.arrayInfo[1]]
                    typeWidth = self.typeSizes[self.arrayInfo[0]]
                    typeWidthAddr = self.createAddrLiteral(str(typeWidth))
                    self.addQuad('*', expressionAddr, typeWidthAddr, arrayTempAddr)

                    otherTemp = self.getNewTemp()
                    otherTempAddr = self.createAddrLiteral(otherTemp)
                    self.addQuad('+', tempAddr, arrayTempAddr, otherTempAddr)

                    self.nodeAddr[ctx] = self.createAddrVar(myvar, otherTemp)
                    self.arrayInfo = []
                    self.currentStructMovement = 0
                else:
                    newTemp = self.getNewTemp()
                    tempAddr = self.createAddrLiteral(newTemp)
                    op1Addr = self.createAddrLiteral(str(self.currentStructMovement))
                    op2Addr = self.createAddrLiteral(str(myvar.offset))
                    self.addQuad('+', op2Addr, op1Addr, tempAddr)

                    self.nodeAddr[ctx] = self.createAddrVar(myvar, newTemp)
                    self.currentStructMovement = 0
            else:
                if (ctx.expression() and isMiddle == False):
                    # Can check array addresses
                    newTemp = self.getNewTemp()
                    tempAddr = self.createAddrLiteral(newTemp)
                    expressionAddr = self.nodeAddr[ctx.expression()]
                    typeWidth = self.typeSizes[myvar.varType]
                    typeWidthAddr = self.createAddrLiteral(str(typeWidth))
                    self.addQuad('*', expressionAddr, typeWidthAddr, tempAddr)

                    otherTemp = self.getNewTemp()
                    otherTempAddr = self.createAddrLiteral(otherTemp)
                    offsetAddr = self.createAddrLiteral(str(myvar.offset))
                    self.addQuad('+', tempAddr, offsetAddr, otherTempAddr)

                    print("array " + ctx.getText(), str(ctx.start.line))
                    self.nodeAddr[ctx] = self.createAddrVar(myvar, otherTemp)
                else:
                    self.nodeAddr[ctx] = self.createAddrVar(myvar, myvar.offset)

    def exitVarDeclaration(self, ctx: DecafParser.VarDeclarationContext):
        varType = ctx.getChild(0).getText()
        self.nodeTypes[ctx] = varType          

    def exitExpr_loc(self, ctx: DecafParser.Expr_locContext):
        self.nodeTypes[ctx] = self.nodeTypes[ctx.getChild(0)]
        self.nodeAddr[ctx] = self.nodeAddr[ctx.getChild(0)]

    def exitExpr_mcall(self, ctx: DecafParser.Expr_mcallContext):
        self.nodeTypes[ctx] = self.nodeTypes[ctx.getChild(0)]   

    """ Operations """
    # NOTE: Se debe de saltar un nodo siempre porque no se está tomando en cuenta el expression padre, se debe obtener el t ipo de los literals.
    # * / %
    def exitExpr_arith5(self, ctx: DecafParser.Expr_arith5Context):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)
        operator = ctx.getChild(1).getText()

        if(self.nodeTypes[op1] == 'int' and self.nodeTypes[op2] == 'int'):
            # Validar el tipo de expression (operador) expression, ver si ambos son int
            # Una vez se validó, lo podemos agregar a nuestro diccionario
            self.nodeTypes[ctx] = 'int'
            
            """ Code generation """
            # First, generate a new Temp() according to operator rules.
            newTemp = self.getNewTemp()
            # Set address of node to newTemp
            self.nodeAddr[ctx] = self.createAddrLiteral(newTemp)
            # Generate quad
            self.addQuad(operator, self.nodeAddr[op1], self.nodeAddr[op2], self.nodeAddr[ctx])
        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error'
            self.addError((ctx.start.line, "typingNoMatch"), "Operation expected two integer typed operators.")  

    # + -
    def exitExpr_arith4(self, ctx: DecafParser.Expr_arith4Context):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)
        operator = ctx.getChild(1).getText()

        if(self.nodeTypes[op1] == 'int' and self.nodeTypes[op2] == 'int'):
            # Validar el tipo de expression (operador) expression, ver si ambos son int
            # Una vez se validó, lo podemos agregar a nuestro diccionario
            self.nodeTypes[ctx] = 'int'

            """ Code generation """
            # First, generate a new Temp() according to operator rules.
            newTemp = self.getNewTemp()
            # Set address of node to newTemp
            self.nodeAddr[ctx] = self.createAddrLiteral(newTemp)
            # Generate quad
            self.addQuad(operator, self.nodeAddr[op1], self.nodeAddr[op2], self.nodeAddr[ctx])
        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error'
            self.addError((ctx.start.line, "typingNoMatch"), "Operation expected two integer typed operators.")    
            return 

    # eq_op: == != | rel_op: < <= > >=
    def exitExpr_arith3(self, ctx: DecafParser.Expr_arith3Context):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)
        symbol = ctx.getChild(1).getText()

        if (symbol == '<' or symbol == '<=' or symbol == '>' or symbol == '>='):
            if(self.nodeTypes[op1] == 'int' and self.nodeTypes[op2] == 'int'):
                # Validar el tipo de expression (operador) expression, ver si ambos son int
                # Una vez se validó, lo podemos agregar a nuestro diccionario
                self.nodeTypes[ctx] = 'boolean'

                self.addQuad(symbol, self.nodeAddr[op1], self.nodeAddr[op2], self.nodeAddr[ctx])
                self.addQuad('gotof', self.nodeAddr[ctx], None, None)
                self.relCounter += 1
            else:
                # Si no pues es un error.
                self.nodeTypes[ctx] = 'error'
                self.addError((ctx.start.line, "typingNoMatch"), "Operation expected two integer typed operators.")
        elif (symbol == "==" or symbol == "!="):
            allowed = ('int', 'char', 'boolean')
            type1 = self.nodeTypes[op1] 
            type2 = self.nodeTypes[op2]

            # Chequear tipos permitidos
            if (type1 in allowed and type2 in allowed):
                if(self.nodeTypes[op1] == self.nodeTypes[op2]):
                    # Una vez se validó, lo podemos agregar a nuestro diccionario
                    self.nodeTypes[ctx] = 'boolean'

                    self.addQuad(symbol, self.nodeAddr[op1], self.nodeAddr[op2], self.nodeAddr[ctx])
                    self.addQuad('gotof', self.nodeAddr[ctx], None, None)
                    self.relCounter += 1
                else:
                    # Si no pues es un error.
                    self.nodeTypes[ctx] = 'error'
                    self.addError((ctx.start.line, "typingNoMatch"), "Operation expected two integer typed operators.")  
            # Si no está entre los permitidos, es error
            else:
                self.nodeTypes[ctx] = 'error'
                self.addError((ctx.start.line, "typingNoMatch"), "One of the operators has a type not accepted by the language.")      

    # &&
    def exitExpr_arith2(self, ctx: DecafParser.Expr_arith2Context):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)

        if(self.nodeTypes[op1] == 'boolean' and self.nodeTypes[op2] == 'boolean'):
            # Validar el tipo de expression (operador) expression, ver si ambos son int
            # Una vez se validó, lo podemos agregar a nuestro diccionario
            self.nodeTypes[ctx] = 'boolean'
        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error' 
            self.addError((ctx.start.line, "typingNoMatch"), "Operation expected two boolean typed operators.")   

    # ||
    def exitExpr_arith1(self, ctx: DecafParser.Expr_arith1Context):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)

        if(self.nodeTypes[op1] == 'boolean' and self.nodeTypes[op2] == 'boolean'):
            # Validar el tipo de expression (operador) expression, ver si ambos son int
            # Una vez se validó, lo podemos agregar a nuestro diccionario
            self.nodeTypes[ctx] = 'boolean'
        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error'
            self.addError((ctx.start.line, "typingNoMatch"), "Operation expected two boolean typed operators.")

    # !
    def exitExpr_not(self, ctx: DecafParser.Expr_notContext):
        op1 = ctx.getChild(1)

        if(self.nodeTypes[op1] == 'boolean'):
            # Validar el tipo de expression (operador) expression, ver si ambos son int
            # Una vez se validó, lo podemos agregar a nuestro diccionario
            self.nodeTypes[ctx] = 'boolean'
        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error'
            self.addError((ctx.start.line, "typingNoMatch"), "!: Operation expected a boolean typed operator.")

    def exitExpr_minus(self, ctx: DecafParser.Expr_minusContext):
        op1 = ctx.getChild(1)

        if(self.nodeTypes[op1] == 'int'):
            # Validar el tipo de expression (operador) expression, ver si ambos son int
            # Una vez se validó, lo podemos agregar a nuestro diccionario
            self.nodeTypes[ctx] = 'int'

            """ Code generation """
            # First, generate a Temp according to operator rules´.
            newTemp = self.getNewTemp()
            # Set address of node to newTemp
            self.nodeAddr[ctx] = self.createAddrLiteral(newTemp)
            # Generate quad according to rule
            self.addQuad('minus', self.nodeAddr[op1], None, self.nodeAddr(ctx))

        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error'
            self.addError((ctx.start.line, "typingNoMatch"), "-: Operation expected an int typed operator.")

    def exitExpr_parenthesis(self, ctx: DecafParser.Expr_parenthesisContext):
        self.nodeTypes[ctx] = self.nodeTypes[ctx.expression()]

        """ Code generation """
        # Generate addr and set it to the same
        self.nodeAddr[ctx] = self.nodeAddr[ctx.expression()]

    def exitStat_assignment(self, ctx: DecafParser.Stat_assignmentContext):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)

        if(self.nodeTypes[op1] == self.nodeTypes[op2]):
            # Validar el tipo de expression (operador) expression, ver si ambos son int
            # Una vez se validó, lo podemos agregar a nuestro diccionario
            self.nodeTypes[ctx] = self.nodeTypes[op1]

            """ Code generation """
            # Only code generation, there is no setting addresses for this rule.
            # top.get(id)
            self.addQuad('', self.nodeAddr[op2], None, self.nodeAddr[op1])
            #op1Var = self.lookupVarInSymbolTable(op1, self.currentScope)
            #if (op1Var != None):         
        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error'
            self.addError((ctx.start.line ,"typingNoMatch"), "Assigment should be of the same type on its operands.")
            return

    # 'if' '(' expression ')' block | ( 'else' block )? 
    def exitStat_if(self, ctx: DecafParser.Stat_ifContext):
        expression = ctx.getChild(2)
        statement = ctx.getChild(4)

        if(self.nodeTypes[expression] == 'boolean'):
            self.nodeTypes[ctx] = 'boolean'

            """ Code generation """
            nextAddr = self.nodeAddr[statement] 

            self.addQuad("labeln", nextAddr, None, None)
            self.blockCounter += 1
            self.firstCheck = False 
        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error' 
            self.addError((ctx.start.line ,"typingNoMatch"), "if statement should be a boolean expression.") 

    # This should be exitStat_while but it was tagged incorrectly in the grammar.
    def exitStat_else(self, ctx: DecafParser.Stat_elseContext):
        expression = ctx.getChild(2)

        if(self.nodeTypes[expression] == 'boolean'):
            self.nodeTypes[ctx] = 'boolean'

            """ Code generation """
            self.addQuad("goton", self.nodeAddr[ctx.getChild(4)], None, None)
            self.addQuad("labelf", self.nodeAddr[expression], None, None)

            self.blockCounter += 1
        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error'
            self.addError((ctx.start.line ,"typingNoMatch"), "while statement should be a boolean expression.")
        
    """ Literals """
    def exitInt_literal(self, ctx: DecafParser.Int_literalContext):
        self.nodeTypes[ctx] = 'int'
        self.nodeAddr[ctx] = self.createAddrLiteral(ctx.getText())

    def exitChar_literal(self, ctx: DecafParser.Char_literalContext):
        self.nodeTypes[ctx] = 'char'
        self.nodeAddr[ctx] = self.createAddrLiteral(ctx.getText())

    def exitBool_literal(self, ctx: DecafParser.Bool_literalContext):
        self.nodeTypes[ctx] = 'boolean'
        self.nodeAddr[ctx] = self.createAddrLiteral(ctx.getText())
    
    def exitLiteral(self, ctx: DecafParser.LiteralContext):
        self.nodeTypes[ctx] = self.nodeTypes[ctx.getChild(0)]
        self.nodeAddr[ctx] = self.nodeAddr[ctx.getChild(0)]

    def exitExpr_literal(self, ctx: DecafParser.Expr_literalContext):
        self.nodeTypes[ctx] = self.nodeTypes[ctx.getChild(0)]
        self.nodeAddr[ctx] = self.nodeAddr[ctx.getChild(0)]

    # -----------------------------------------------------------------------
    # Non override methods
    def enterScope(self, scope):
        self.pastScope = self.currentScope
        self.currentScope = scope

    def calculateSize(self, varType, num):
        num = int(num)
        if varType in self.typeSizes:
            return self.typeSizes[varType]*num
        elif (varType in self.structDictionary):
            return self.structDictionary[varType].size*num

    # Expects a key (line, type) and body (string)
    def addError(self, key, body):
        if (key not in self.errorDictionary):
            self.errorDictionary[key] = body 

    def getRootMethod(self, scope):
        scopeObject = self.scopeDictionary.get(scope)

        if (scopeObject.parentKey != "global"):
            scopeObject = self.getRootMethod(scopeObject.parentKey)

        return scopeObject

    def checkMethodParameters(self, scope, checkId):
        isInParams = False
        rootMethod = self.getRootMethod(scope)
        rmSymbolTable = rootMethod.symbolTable
        paramList = []

        for varId, varObj in rmSymbolTable.items():
            if varObj.varContext == "param":
                paramList.append(varObj.varId)

        if checkId in paramList: isInParams = True 
        
        return isInParams

    def checkGlobalVars(self, varId):
        isInGlobal = False
        tempSymbolTable = self.scopeDictionary.get("global").symbolTable

        if varId in tempSymbolTable:
            isInGlobal = True

        return isInGlobal

    def compareParameters(self, methodObj, args, methodCallTypes):
        symbolTable = methodObj.symbolTable
        methodDeclarationTypes = []

        # Conseguimos los parametros del método
        for varId, varItem in symbolTable.items():
            if varItem.varContext == "param":
                methodDeclarationTypes.append(varItem.varType)

        if (methodCallTypes == methodDeclarationTypes):
            return True 
        else:
            return False

  
    # -----------------------------------------------------------------------
    # Symbol Table related methods
    def addScopeToSymbolTable(self, pastScope, methodType=None):
        canAdd = False
        if self.currentScope not in self.scopeDictionary:
            self.scopeDictionary[self.currentScope] = SymbolTableItem(parentKey=pastScope, returnType=methodType, symbolTable={})
            canAdd = True
        else:
            canAdd = False

        return canAdd

    def addVarToSymbolTable(self, varType, varId, varContext, num, isArray, scope):
        if (num == None): num = 1
        canAdd = False
        currentVarSize = self.calculateSize(varType, num)

        currentOffset = 0

        if (self.currentScope == 'global'):
            currentOffset = self.globalOffset
        else:
            currentOffset = self.localOffset

        # Gets the SymbolTable from the current scope
        tempSymbolTable = self.scopeDictionary.get(self.currentScope).symbolTable

        if varId not in tempSymbolTable:
            tempSymbolTable[varId] = VarSymbolTableItem(varId, varType, varContext, num, currentVarSize, isArray, currentOffset, scope)
            if (self.currentScope == 'global'):
                self.globalOffset += currentVarSize
            else:
                self.localOffset += currentVarSize
            canAdd = True
        else:
            canAdd = False

        self.scopeDictionary.get(self.currentScope).symbolTable = tempSymbolTable
        return canAdd

    # Needs to search this recursively
    # Initial call will be made with currentScope
    def lookupVarInSymbolTable(self, varId, scopeName):
        # Gets the SymbolTable 
        tempSymbolTable = self.scopeDictionary.get(scopeName).symbolTable
        searchedVar = None

        # Procedure for a normal var
        if varId in tempSymbolTable:
            searchedVar = tempSymbolTable[varId]
        else:
            newScope = self.scopeDictionary.get(scopeName).parentKey

            if (newScope != None):
                searchedVar = self.lookupVarInSymbolTable(varId, newScope)

        return searchedVar

    def updateVarInSymbolTable(self, varId, varValue, scopeName):
        print("updating value")

    def lookupMethodInSymbolTable(self, methodId):
        scopeObject = self.scopeDictionary.get(methodId)
        return scopeObject

    #-------------------------------
    # Structs

    # Grammar saves a struct variable as
    #   struct+ID
    # So we're adding a struct prefix to make it match the grammar. For example, struct "A" will be saved as "structA" in the struct dictionary.
    # This is so if we have a var saved with type structA, it will look it up directly instead of adding the prefix when searching.
    def addStructToSymbolTable(self, structId):
        structId = "struct"+structId
        if structId not in self.structDictionary:
            self.structDictionary[structId] = StructSymbolTableItem(structId=structId, structMembers={})

    def addVarToStruct(self, structId, varType, varId, varContext, num, isArray, scope):
        if (num == None): num = 1
        canAdd = False
        currentVarSize = self.calculateSize(varType, num)

        currentOffset = self.structOffset

        structId = "struct"+structId
        tempStructMembers = self.structDictionary.get(structId).structMembers
        tempStructSize = self.structDictionary.get(structId).size

        if varId not in tempStructMembers:
            tempStructMembers[varId] = VarSymbolTableItem(varId, varType, varContext, num, currentVarSize, isArray, currentOffset, scope)
            self.structOffset += currentVarSize
            tempStructSize += currentVarSize
            canAdd = True
        else:
            canAdd = False

        self.structDictionary.get(structId).structMembers = tempStructMembers
        self.structDictionary.get(structId).size = tempStructSize
        return canAdd

    def searchStructMember(self, structId):
        structMember = None
        if structId in self.structDictionary:
            structMember = self.structDictionary[structId]

        return structMember

    # -------------------------------
    # Intermediate code generation
    def addQuad(self, op, arg1, arg2, result):
        quad = QuadBucket(op, arg1, arg2, result)
        self.quadList.append(quad)


    def getCodeContext(self, var):
        if (var.scope == 'global'):
            codeContext = "G"
        else:
            codeContext = "L"

        return codeContext

    def createAddrVar(self, var, memoryLoc):
        codeContext = self.getCodeContext(var)
        addrString = codeContext+"["+str(memoryLoc)+"]"
        addr = AddrEntry(addrString, None, None, None)
        return addr

    def createAddrLiteral(self, literal):
        addr = AddrEntry(literal, None, None, None)
        return addr

    def createAddrLabels(self, lblTrue, lblFalse):
        addr = AddrEntry(None, lblTrue, lblFalse, None)
        return addr

    def createAddrNext(self, lblNext):
        addr = AddrEntry(None, None, None, lblNext)
        return addr

    def getNewTemp(self):
        tempName = "t" + str(self.tempCounter)
        self.tempCounter += 1
        return tempName

    def createLabel(self, label_name):
        newLabel = "l_"+label_name
        return newLabel

    def getCodeFromQuad(self, quad):
        quadString = ""

        if (quad.op == '<' or quad.op== '<=' or quad.op == '>' or quad.op == '>=' or quad.op == '==' or quad.op == '!='):
            quadString = '  if ' + quad.arg1.addr + quad.op + quad.arg2.addr + ' goto ' + quad.result.lblTrue
        elif (quad.op == "label"):
            if (quad.arg1 != None):
                quadString = quad.arg1.addr + ":"
        elif (quad.op == "labelt"):
            quadString = quad.arg1.lblTrue + ":"
        elif (quad.op == "labelf"):
            quadString = quad.arg1.lblFalse + ":"
        elif (quad.op == "labeln"):
            quadString = quad.arg1.lblNext + ":"
        elif (quad.op == "goton"):
            quadString = "  goto " + quad.arg1.lblNext
        elif (quad.op == "gotof"):
            quadString = "  goto " + quad.arg1.lblFalse
        elif (quad.result == None):
            quadString = "  " + quad.op + " " + quad.arg1.addr
        elif (quad.arg2 != None):
            quadString = "  " + quad.result.addr + "=" + quad.arg1.addr  + quad.op + quad.arg2.addr 
        elif (quad.arg2 == None):
            quadString = "  " + quad.result.addr + "=" + quad.op + quad.arg1.addr 

        return quadString 
#---------------------------------------------------------------------------------------------------

def check(argv):
    input_stream = FileStream(argv)
    lexer = DecafLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DecafParser(stream)
    tree = parser.program()  
    printer = DecafPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


    print("--------------------------------------------")
    print("SYMBOL TABLE \n")
    
    for c, v in printer.scopeDictionary.items():
        print("KEY: ", c)
        print("     Parent scope: ", v.parentKey)
        print("     Return type: ", v.returnType)
        print("     Items: ")
        for var, varItem in v.symbolTable.items():
            print("         VarId: " + var + ", VarType: " + varItem.varType + ", Num: " + str(varItem.num) + ", Size: " + str(varItem.size) + ", isArray: " + str(varItem.isArray) + ", Offset: " + str(varItem.offset))

    print("--------------------------------------------")
    print("STRUCT INFORMATION \n")

    for c, v in printer.structDictionary.items():
        print("STRUCT: ", c)
        print("     Items: ")
        for var, varItem in v.structMembers.items():
            print("         VarId: " + var + ", VarType: " + varItem.varType + ", Num: " + str(varItem.num) + ", Size: " + str(varItem.size) + ", isArray: " + str(varItem.isArray) + ", Offset: " + str(varItem.offset))

    print("--------------------------------------------")

    quadTranslated = []
    for quad in printer.quadList:
        quadTranslated.append(printer.getCodeFromQuad(quad)+"\n")

    #traverse(tree, parser.ruleNames)
    return printer.errorDictionary, quadTranslated

def traverse(tree, rule_names, indent = 0):
    if tree.getText() == "<EOF>":
        return
    elif isinstance(tree, TerminalNode):
        print("{0}T='{1}'".format("  " * indent, tree.getText()))
    else:
        print("{0}R='{1}'".format("  " * indent, rule_names[tree.getRuleIndex()]))
        if (tree.children != None):
            for child in tree.children:
                traverse(child, rule_names, indent + 1)


