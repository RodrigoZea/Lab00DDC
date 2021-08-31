import sys
import re
from antlr4 import *
from antlr4.tree.Trees import TerminalNode
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.ErrorStrategy import ErrorStrategy, DefaultErrorStrategy
from antlr4.error.Errors import *
from DecafLexer import DecafLexer
from DecafParser import DecafParser
from DecafListener import DecafListener
from DecafErrors import *

# Stack
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
    def __init__(self, varId, varType, varContext, num, size):
        self.varId = varId 
        self.varType = varType
        self.value = None
        self.num = num
        self.size = size
        self.offset = 0
        self.varContext = varContext

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

#---------------------------------------------------------------------------------------------------

class DecafPrinter(DecafListener):
    def __init__(self) -> None:
        # Flags or misc
        self.errorList = []
        self.primitives = ('int', 'char', 'boolean', 'struct', 'void')
        self.typeSizes = {'int':4, 'char':1, 'boolean':1}
        self.startingValues = {'int': '0', 'boolean': 'false', 'char': 'a'}
        self.nodeTypes = {}
        self.mainFound = False
        self.structToUse = None

        # Symbol table related
        self.currentMethodName = ""
        self.currentScope = "global"
        self.pastScope = "None"
        self.nestedCounter = 1
        self.scopeDictionary = {}
        self.structDictionary = {}

        self.addScopeToSymbolTable(None)

        super().__init__()

    def returnErrorList(self):
        return self.errorList

    # -----------------------------------------------------------------------
    # Listener override methods
    def enterVarDeclaration(self, ctx: DecafParser.VarDeclarationContext):
        value = None
        if (ctx.NUM() != None):
            value = ctx.getChild(3).getText()

            if (int(value) <= 0):
                self.nodeTypes[ctx] = 'error'
                self.addError(ctx.start.line, "Array size must be bigger than 0")
                return

        parentCtx = ctx.parentCtx
        firstChild = parentCtx.getChild(0).getText()

        varType = ctx.getChild(0).getText()
        varId = ctx.getChild(1).getText()

        if firstChild == "struct":
            structId = parentCtx.getChild(1).getText()
            added = self.addVarToStruct(structId, varType, varId, "blockVar", value)

            if (added):
                self.nodeTypes[ctx] = 'void'
            else:
                self.nodeTypes[ctx] = 'error'
                self.addError(ctx.start.line, "Failed to add variable to struct, variable already exists.")
        else:
            added = self.addVarToSymbolTable(varType, varId, "blockVar", value)

            if (added):
                self.nodeTypes[ctx] = 'void'
            else:
                self.nodeTypes[ctx] = 'error'
                self.addError(ctx.start.line, "Failed to add variable to scope, variable already exists.")

 
    def enterMethodDeclaration(self, ctx: DecafParser.MethodDeclarationContext):
        methodType = ctx.getChild(0).getText()
        methodName = ctx.getChild(1).getText()

        self.currentMethodName = methodName
        self.enterScope(methodName)

        # Add to symbol table!
        added = self.addScopeToSymbolTable(self.pastScope, methodType)

        if (added):
            self.nodeTypes[ctx] = 'void'
        else:
            self.nodeTypes[ctx] = 'error'
            self.addError(ctx.start.line, "Failed to add method to symbol table, there's already a method with that name.")

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

        # TODO: Check weird error with not adding scope
        if (added):
            self.nodeTypes[ctx] = 'void'

    def enterParameter(self, ctx: DecafParser.ParameterContext):
        paramType = ctx.getChild(0).getText()

        if paramType != 'void':
            paramId = ctx.getChild(1).getText()

            added = self.addVarToSymbolTable(paramType, paramId, "param", None)
            if (added):
                self.nodeTypes[ctx] = 'void'
            else:
                # TODO: Add error
                self.nodeTypes[ctx] = 'error'
                self.addError(ctx.start.line, "Failed to add parameter to symbol table, there's already an existing parameter with that name.")

    def enterStructDeclaration(self, ctx: DecafParser.StructDeclarationContext):
        structId = ctx.getChild(1).getText()
        self.addStructToSymbolTable(structId)

    def enterLocation(self, ctx: DecafParser.LocationContext):
        anotherLocation = False
        for child in ctx.children:
            if type(child) == DecafParser.LocationContext:
                anotherLocation = True

        if (type(ctx.parentCtx) == DecafParser.LocationContext and anotherLocation):
            newStructToUse = self.structToUse.structMembers[ctx.getChild(0).getText()]
            self.structToUse = self.searchStructMember(newStructToUse.varType)
        elif (ctx.location()):
            varId = ctx.getChild(0).getText()
            structVarType = self.lookupVarInSymbolTable(varId, self.currentScope)
            self.structToUse = self.searchStructMember(structVarType.varType)

    # ----------------------------------------------------------------------
    # Exit
    def exitMethodDeclaration(self, ctx: DecafParser.MethodDeclarationContext):
        methodName = ctx.getChild(1).getText()
        if (methodName == 'main'):
            self.mainFound = True

        self.nestedCounter = 1
        self.currentMethodName = "global"

        self.enterScope("global")

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


            # TODO: Check with more than 1 arg and no args
            paramsEquality = self.compareParameters(methodObj, args, methodCallTypes)

            if paramsEquality:
                self.nodeTypes[ctx] = methodObj.returnType
            else:
                self.nodeTypes[ctx] = 'error'
                self.addError(ctx.start.line, "Failed to call method, parameters don't match (either in type or order is incorrect)")
        else:
            self.nodeTypes[ctx] = 'error'
            self.addError(ctx.start.line, "Method doesn't exist in symbol table or hasn't been declared yet.")
        
    def exitProgram(self, ctx: DecafParser.ProgramContext):
        if (not self.mainFound):
            self.nodeTypes[ctx] = 'error'
            self.addError(ctx.start.line, "Main method is not declared!")

    def exitStat_return(self, ctx: DecafParser.StatementContext):
        # Children structure
        # 0: Return
        # 1: Value
        # 2: ;
        # Everything related to returns
        if ctx.getChild(0).getText() == "return":
            rootMethod = self.getReturnTypeOfMethod(self.currentScope)
            methodType = rootMethod.returnType
            expressionOom = ctx.getChild(1)

            if (ctx.getChild(1).getText() == ""):
                if (methodType == 'void'):
                    self.nodeTypes[ctx] = 'void'
                elif(methodType in self.primitives):
                    self.nodeTypes[ctx] = 'error'
                    self.addError(ctx.start.line, "Typed method expecting a return value.")
                else:
                    self.nodeTypes[ctx] = 'error' 
                    self.addError(ctx.start.line, "Method type is not accepted by language.")     
            else:
                if (methodType in self.primitives):
                    exprType = self.nodeTypes[expressionOom.getChild(0)]

                    if (exprType == methodType):
                        self.nodeTypes[ctx] = 'void'
                    else:
                        self.nodeTypes[ctx] = 'error'
                        self.addError(ctx.start.line, "Return statement type doesn't match with method type.")
                else:
                    self.nodeTypes[ctx] = 'error' 
                    self.addError(ctx.start.line, "Method type is not accepted by language.")                      

    # NOTE: Se debe de saltar un nodo siempre porque no se está tomando en cuenta el expression padre, se debe obtener el t ipo de los literals.
    # * / %
    def exitExpr_arith5(self, ctx: DecafParser.Expr_arith5Context):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)

        if(self.nodeTypes[op1] == 'int' and self.nodeTypes[op2] == 'int'):
            # Validar el tipo de expression (operador) expression, ver si ambos son int
            # Una vez se validó, lo podemos agregar a nuestro diccionario
            self.nodeTypes[ctx] = 'int'
        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error'
            self.addError(ctx.start.line, "Operation expected two integer typed operators.")     
    # + -
    def exitExpr_arith4(self, ctx: DecafParser.Expr_arith5Context):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)

        if(self.nodeTypes[op1] == 'int' and self.nodeTypes[op2] == 'int'):
            # Validar el tipo de expression (operador) expression, ver si ambos son int
            # Una vez se validó, lo podemos agregar a nuestro diccionario
            self.nodeTypes[ctx] = 'int'
        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error'
            self.addError(ctx.start.line, "Operation expected two integer typed operators.")    

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
            else:
                # Si no pues es un error.
                self.nodeTypes[ctx] = 'error'
                self.addError(ctx.start.line, "Operation expected two integer typed operators.")    
        elif (symbol == "==" or symbol == "!="):
            allowed = ('int', 'char', 'boolean')
            type1 = self.nodeTypes[op1] 
            type2 = self.nodeTypes[op2]

            # Chequear tipos permitidos
            if (type1 in allowed and type2 in allowed):
                if(self.nodeTypes[op1] == self.nodeTypes[op2]):
                    # Una vez se validó, lo podemos agregar a nuestro diccionario
                    self.nodeTypes[ctx] = 'boolean'
                else:
                    # Si no pues es un error.
                    self.nodeTypes[ctx] = 'error'
                    self.addError(ctx.start.line, "Operation expected two operators with the same type.")    
            # Si no está entre los permitidos, es error
            else:
                self.nodeTypes[ctx] = 'error'
                self.addError(ctx.start.line, "One of the operators has a type not accepted by the language.")    

    # &&
    def exitArith_op_second(self, ctx: DecafParser.Arith_op_secondContext):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)

        if(self.nodeTypes[op1] == 'boolean' and self.nodeTypes[op2] == 'boolean'):
            # Validar el tipo de expression (operador) expression, ver si ambos son int
            # Una vez se validó, lo podemos agregar a nuestro diccionario
            self.nodeTypes[ctx] = 'boolean'
        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error'
            self.addError(ctx.start.line, "Operation expected two boolean typed operators.")    

    # ||
    def exitArith_op_first(self, ctx: DecafParser.Arith_op_firstContext):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)

        if(self.nodeTypes[op1] == 'boolean' and self.nodeTypes[op2] == 'boolean'):
            # Validar el tipo de expression (operador) expression, ver si ambos son int
            # Una vez se validó, lo podemos agregar a nuestro diccionario
            self.nodeTypes[ctx] = 'boolean'
        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error'
            self.addError(ctx.start.line, "Operation expected two boolean typed operators.")   

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
            self.addError(ctx.start.line, "Operation expected a boolean typed operator.")   

    def exitExpr_parenthesis(self, ctx: DecafParser.Expr_parenthesisContext):
        self.nodeTypes[ctx] = self.nodeTypes[ctx.expression()]
        
    def exitInt_literal(self, ctx: DecafParser.Int_literalContext):
        self.nodeTypes[ctx] = 'int'

    def exitChar_literal(self, ctx: DecafParser.Char_literalContext):
        self.nodeTypes[ctx] = 'char'

    def exitBool_literal(self, ctx: DecafParser.Bool_literalContext):
        self.nodeTypes[ctx] = 'boolean'

    def exitExpr_loc(self, ctx: DecafParser.Expr_locContext):
        self.nodeTypes[ctx] = self.nodeTypes[ctx.getChild(0)]
        
    def exitLocation(self, ctx: DecafParser.LocationContext):
        if (ctx.expression()):
            if (self.nodeTypes[ctx.expression()] != 'int'):
                self.nodeTypes[ctx] = 'error'
                self.addError(ctx.start.line, "<expr> in ID[<expr>] must be of type int.")  
                return 

        if (type(ctx.parentCtx) == DecafParser.LocationContext and ctx.location() != None):
            if self.structToUse != None:
                self.nodeTypes[ctx] = self.nodeTypes[ctx.location()]
        elif (type(ctx.parentCtx) == DecafParser.LocationContext):
            if self.structToUse != None:
                myvar = self.structToUse.structMembers[ctx.getChild(0).getText()]
                if (myvar != None):
                    self.nodeTypes[ctx] = myvar.varType
        elif (ctx.location() != None):
            if self.structToUse != None:
                self.nodeTypes[ctx] = self.nodeTypes[ctx.location()]
        else:
            myvar = self.lookupVarInSymbolTable(ctx.getChild(0).getText(), self.currentScope)
            if (myvar != None):
                self.nodeTypes[ctx] = myvar.varType
            else:
                self.nodeTypes[ctx] = 'error'
                self.addError(ctx.start.line, "Variable hasn't been defined yet.")   


    def exitVarDeclaration(self, ctx: DecafParser.VarDeclarationContext):
        varType = ctx.getChild(0).getText()
        self.nodeTypes[ctx] = varType

    def exitLiteral(self, ctx: DecafParser.LiteralContext):
        self.nodeTypes[ctx] = self.nodeTypes[ctx.getChild(0)]

    def exitExpr_literal(self, ctx: DecafParser.Expr_literalContext):
        self.nodeTypes[ctx] = self.nodeTypes[ctx.getChild(0)]

    def exitExpr_mcall(self, ctx: DecafParser.Expr_mcallContext):
        self.nodeTypes[ctx] = self.nodeTypes[ctx.getChild(0)]
    

    def exitStat_assignment(self, ctx: DecafParser.Stat_assignmentContext):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)

        if(self.nodeTypes[op1] == self.nodeTypes[op2]):
            # Validar el tipo de expression (operador) expression, ver si ambos son int
            # Una vez se validó, lo podemos agregar a nuestro diccionario
            self.nodeTypes[ctx] = self.nodeTypes[op1]
        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error'
            self.addError(ctx.start.line, "Assigment should be of the same type on its operands.")   

    def exitStat_if(self, ctx: DecafParser.Stat_ifContext):
        expression = ctx.getChild(2)

        if(self.nodeTypes[expression] == 'boolean'):
            self.nodeTypes[ctx] = 'boolean'
        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error'
            self.addError(ctx.start.line, "if statement should be a boolean expression.")         


    # This should be exitStat_while but it was tagged incorrectly in the grammar.
    def exitStat_else(self, ctx: DecafParser.Stat_elseContext):
        expression = ctx.getChild(2)

        if(self.nodeTypes[expression] == 'boolean'):
            self.nodeTypes[ctx] = 'boolean'
        else:
            # Si no pues es un error.
            self.nodeTypes[ctx] = 'error'
            self.addError(ctx.start.line, "while statement should be a boolean expression.")     

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

    def addError(self, line, body):
        errorMsg = "Error at line (" + str(line) + "): " + body
        self.errorList.append(errorMsg)
  
    # -----------------------------------------------------------------------
    # TODO: Offsets...
    # Symbol Table related methods
    def addScopeToSymbolTable(self, pastScope, methodType=None):
        canAdd = False
        if self.currentScope not in self.scopeDictionary:
            self.scopeDictionary[self.currentScope] = SymbolTableItem(parentKey=pastScope, returnType=methodType, symbolTable={})
            canAdd = True
        else:
            canAdd = False

        return canAdd

    def addVarToSymbolTable(self, varType, varId, varContext, num):
        if (num == None): num = 1
        canAdd = False
        currentVarSize = self.calculateSize(varType, num)

        # Gets the SymbolTable from the current scope
        tempSymbolTable = self.scopeDictionary.get(self.currentScope).symbolTable

        if varId not in tempSymbolTable:
            tempSymbolTable[varId] = VarSymbolTableItem(varId, varType, varContext, num, currentVarSize)
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

    def getReturnTypeOfMethod(self, scope):
        scopeObject = self.scopeDictionary.get(scope)

        if (scopeObject.parentKey != "global"):
            scopeObject = self.getReturnTypeOfMethod(scopeObject.parentKey)

        return scopeObject
        

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

    def addVarToStruct(self, structId, varType, varId, varContext, num):
        if (num == None): num = 1
        canAdd = False
        currentVarSize = self.calculateSize(varType, num)

        structId = "struct"+structId
        tempStructMembers = self.structDictionary.get(structId).structMembers
        tempStructSize = self.structDictionary.get(structId).size

        if varId not in tempStructMembers:
            tempStructMembers[varId] = VarSymbolTableItem(varId, varType, varContext, num, currentVarSize)
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

    """
    for c, v in printer.scopeDictionary.items():
        print("KEY: ", c)
        print("     Parent scope: ", v.parentKey)
        print("     Return type: ", v.returnType)
        print("     Items: ")
        for var, varItem in v.symbolTable.items():
            print("         VarId: " + var + ", VarType: " + varItem.varType + ", Num: " + str(varItem.num) + ", Size: " + str(varItem.size))

    print("--------------------------------------------")

    for c, v in printer.structDictionary.items():
        print("STRUCT: ", c)
        print("     Items: ")
        for var, varItem in v.structMembers.items():
            print("         VarId: " + var + ", VarType: " + varItem.varType + ", Num: " + str(varItem.num) + ", Size: " + str(varItem.size))
    """
    for error in printer.errorList:
        print(error)

    #traverse(tree, parser.ruleNames)
    return printer.errorList

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

if __name__ == '__main__':
    main(sys.argv)

