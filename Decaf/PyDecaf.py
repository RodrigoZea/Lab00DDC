import sys
import re
from antlr4 import *
from antlr4.tree.Trees import  TerminalNode
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
        self.boolValues = ('true', 'false')

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
        try:
                value = None
                if (ctx.NUM() != None):
                    value = ctx.getChild(3).getText()
                    # Won't be added to symbol table!
                    if (int(value) <= 0):
                        raise ArraySizeError

                parentCtx = ctx.parentCtx
                firstChild = parentCtx.getChild(0).getText()

                varType = ctx.getChild(0).getText()
                varId = ctx.getChild(1).getText()

                if firstChild == "struct":
                    structId = parentCtx.getChild(1).getText()
                    self.addVarToStruct(structId, varType, varId, "blockVar", value)
                else:
                    self.addVarToSymbolTable(varType, varId, "blockVar", value)

                return super().enterVarDeclaration(ctx)
        except ArraySizeError:
            #print("ArraySizeError at line %d: Array size must be bigger than 0" % ctx.start.line)
            a = 0

    def enterMethodDeclaration(self, ctx: DecafParser.MethodDeclarationContext):
        methodType = ctx.getChild(0).getText()
        methodName = ctx.getChild(1).getText()

        self.currentMethodName = methodName
        self.enterScope(methodName)

        # TODO: Add to symbol table!
        self.addScopeToSymbolTable(self.pastScope, methodType)

        return super().enterMethodDeclaration(ctx)

    def enterBlock(self, ctx: DecafParser.BlockContext):
        parentCtx = ctx.parentCtx
        firstChild = parentCtx.getChild(0).getText()

        # Normal block
        if firstChild not in self.primitives:
            nestedBlockName = self.currentMethodName + str(self.nestedCounter)
            self.nestedCounter += 1
            self.enterScope(nestedBlockName)
        
        # TODO: Add to symbol table!
        self.addScopeToSymbolTable(self.pastScope)

        return super().enterBlock(ctx)
    
    def exitMethodDeclaration(self, ctx: DecafParser.MethodDeclarationContext):
        self.nestedCounter = 1
        self.currentMethodName = "global"

        self.enterScope("global")

        return super().exitMethodDeclaration(ctx)

    def enterParameter(self, ctx: DecafParser.ParameterContext):
        paramType = ctx.getChild(0).getText()

        if paramType != 'void':
            paramId = ctx.getChild(1).getText()
            self.addVarToSymbolTable(paramType, paramId, "param", None)

        return super().enterParameter(ctx)

    def enterStructDeclaration(self, ctx: DecafParser.StructDeclarationContext):
        structId = ctx.getChild(1).getText()
        self.addStructToSymbolTable(structId)
        return super().enterStructDeclaration(ctx)

    def enterMethodCall(self, ctx: DecafParser.MethodCallContext):
        args = ctx.getChild(2).getText()
        #print(args)
        return super().enterMethodCall(ctx)

    def enterStatement(self, ctx: DecafParser.StatementContext):
        try:
            # Children structure
            # 0: Return
            # 1: Value
            # 2: ;

            # Everything related to returns
            if ctx.getChild(0).getText() == "return":
                # Block context
                blockContext = ctx.parentCtx

                methodDeclarationCtx = blockContext.parentCtx
                methodType = methodDeclarationCtx.getChild(0).getText()
                expressionOom = ctx.getChild(1).getText()

                if expressionOom != ";":
                    if methodType in self.primitives:
                        if expressionOom == '':
                            raise ReturnEmpty
                    elif methodType == "void":
                        if expressionOom != '':
                            raise ReturnNotEmpty

                    # TODO: Restructure this after methodType in self.primitives
                    # Check if expressionOom is not a var
                    print("Expression: ", expressionOom)
                    exprType = self.checkType(expressionOom)
            
                    print("Statement return type: ", exprType)
                    if (exprType == "other"):
                        print("Variable")
                        # Check if its an operation
                        # Else its a single var to lookup

                    # if its a var...
                    # Lookup var in symboltable
                    #returnVar = self.lookupVarInSymbolTable(expressionOom, self.currentScope)
                    # Get return type
                    #if (returnVar != None):
                        #print(returnVar.varType)

            return super().enterStatement(ctx)

        except ReturnMissing:
            #print("Expected return statement on method")
            a = 0
        except ReturnEmpty:
            #print("Missing return value on non-void method")
            a = 0
        except ReturnNotEmpty:
           # print("Void type method should have an empty return")
            a = 0

    # -----------------------------------------------------------------------
    # Non override methods
    def enterScope(self, scope):
        self.pastScope = self.currentScope
        self.currentScope = scope

    def checkType(self, varValue):
        if (self.checkInt(varValue) == True):
            return "int"
        elif(varValue in self.boolValues):
            return "bool"
        elif (varValue.startswith("'") and varValue.endswith("'")):
            return "char"
        else:
            return "other"

    def checkInt(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def calculateSize(self, varType, num):
        num = int(num)
        if varType in self.typeSizes:
            return self.typeSizes[varType]*num
        elif (varType in self.structDictionary):
            return self.structDictionary[varType].size*num
  
    # -----------------------------------------------------------------------
    # TODO: Offsets...
    # Symbol Table related methods
    def addScopeToSymbolTable(self, pastScope, methodType=None):
        if self.currentScope not in self.scopeDictionary:
            self.scopeDictionary[self.currentScope] = SymbolTableItem(parentKey=pastScope, returnType=methodType, symbolTable={})

    def addVarToSymbolTable(self, varType, varId, varContext, num):
        if (num == None): num = 1
        currentVarSize = self.calculateSize(varType, num)

        # Gets the SymbolTable from the current scope
        tempSymbolTable = self.scopeDictionary.get(self.currentScope).symbolTable

        if varId not in tempSymbolTable:
            tempSymbolTable[varId] = VarSymbolTableItem(varId, varType, varContext, num, currentVarSize)
        else:
            print("Variable already exists!")

        self.scopeDictionary.get(self.currentScope).symbolTable = tempSymbolTable

    # Needs to search this recursively
    # Initial call will be made with currentScope
    def lookupVarInSymbolTable(self, varId, scopeName):
        # Gets the SymbolTable 
        tempSymbolTable = self.scopeDictionary.get(scopeName).symbolTable

        searchedVar = None

        if varId in tempSymbolTable:
            searchedVar = tempSymbolTable[varId]
        else:
            newScope = self.scopeDictionary.get(scopeName).parentKey

            if (newScope != None):
                searchedVar = self.lookupVarInSymbolTable(varId, newScope)

        return searchedVar

    def updateVarInSymbolTable(self, varId, varValue, scopeName):
        print("updating value")

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
        currentVarSize = self.calculateSize(varType, num)

        structId = "struct"+structId
        tempStructMembers = self.structDictionary.get(structId).structMembers
        tempStructSize = self.structDictionary.get(structId).size

        if varId not in tempStructMembers:
            tempStructMembers[varId] = VarSymbolTableItem(varId, varType, varContext, num, currentVarSize)
            tempStructSize += currentVarSize
        else:
            print("Variable already exists!")

        self.structDictionary.get(structId).structMembers = tempStructMembers
        self.structDictionary.get(structId).size = tempStructSize

#---------------------------------------------------------------------------------------------------

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = DecafLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DecafParser(stream)
    tree = parser.program()  
    printer = DecafPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

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

    #traverse(tree, parser.ruleNames)

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

