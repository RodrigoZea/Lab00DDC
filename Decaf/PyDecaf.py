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
    def __init__(self, varId, varType, scope, varContext):
        self.varId = varId 
        self.varType = varType
        self.scope = scope
        self.offset = 0
        self.varContext = varContext

class MethodSymbolTableItem():
    def __init__(self, methodId, methodType):
        self.methodId = methodId
        self.methodType = methodType

# Comunicación: Scope de SymbolTableItem con MethodId de MethodSymbolTableItem

class StructSymbolTableItem():
    def __init__(self, structId, structMembers):
        self.structId = structId
        self.structMembers = structMembers
        self.size = 0

# Comunicación: varType != primitivo en SymbolTableItem con structId de StructSymbolTableItem
    # Buscar en StructSymbolTable cada variable que le pertenece a la estructura

class SymbolTableItem():
    def __init__(self, parentKey, symbolTable, returnType):
        self.parentKey = parentKey
        self.returnType = returnType
        self.symbolTable = symbolTable

"""
{
    "main": SymbolTableItem(
        parent: "global",
        symbolTable: [var values...]
    ),
    "main1": SymbolTableItem(
        parent: "main",
        symbolTable: []
    )
    "factorial": SymbolTableItem(
        parent: "global",
        symbolTable: [var values...]
    )
}

"""

#---------------------------------------------------------------------------------------------------

class DecafPrinter(DecafListener):
    def __init__(self) -> None:
        # Flags or misc
        self.errorList = []
        self.mainFound = False
        self.currentMethodType = None
        self.primitives = ('int', 'char', 'boolean', 'struct', 'void')

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
                if (ctx.NUM() != None):
                    value = ctx.getChild(3).getText()
                    # Won't be added to symbol table!
                    if (int(value) <= 0):
                        raise ArraySizeError

                parentCtx = ctx.parentCtx
                firstChild = parentCtx.getChild(0).getText()

                varType = ctx.getChild(0).getText()
                varId = ctx.getChild(1).getText()

                print("VAR: ", varId)
                print("First child: ", varType)
                print("----")

                if firstChild == "struct":
                    structId = parentCtx.getChild(1).getText()
                    self.addVarToStruct(structId, varType, varId, "blockVar")
                else:
                    self.addVarToSymbolTable(varType, varId, "blockVar")

                return super().enterVarDeclaration(ctx)
        except ArraySizeError:
            #print("ArraySizeError at line %d: Array size must be bigger than 0" % ctx.start.line)
            a = 0

    def enterMethodDeclaration(self, ctx: DecafParser.MethodDeclarationContext):
        methodType = ctx.getChild(0).getText()
        methodName = ctx.getChild(1).getText()

        self.currentMethodType = methodType

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
        self.currentMethodType = None
        self.currentMethodName = "global"

        self.enterScope("global")

        return super().exitMethodDeclaration(ctx)

    def enterParameter(self, ctx: DecafParser.ParameterContext):
        paramType = ctx.getChild(0).getText()

        if paramType != 'void':
            paramId = ctx.getChild(1).getText()
            self.addVarToSymbolTable(paramType, paramId, "param")

        return super().enterParameter(ctx)

    def enterStructDeclaration(self, ctx: DecafParser.StructDeclarationContext):
        structId = ctx.getChild(1).getText()
        self.addStructToSymbolTable(structId)
        return super().enterStructDeclaration(ctx)

    def enterStatement(self, ctx: DecafParser.StatementContext):
        try:
            # Children structure
            # 0: Return
            # 1: Value
            # 2: ;
            #hasReturnStatement = False
            statementChldn = ctx.getChildren()

            if ctx.getChild(0).getText() != "return":
                raise ReturnMissing

            if self.currentMethodType == 'void':
                if ctx.getChild(0).getText() == "return" and ctx.getChild(1).getText() != '':
                    raise ReturnNotEmpty
            else:
                if ctx.getChild(1).getText() == '':
                    raise ReturnEmpty

            #self.lookupSymbolTableVar()

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

    # -----------------------------------------------------------------------
    # Symbol Table related methods
    def addScopeToSymbolTable(self, pastScope, methodType=None):
        if self.currentScope not in self.scopeDictionary:
            self.scopeDictionary[self.currentScope] = SymbolTableItem(parentKey=pastScope, returnType=methodType, symbolTable={})

    def addVarToSymbolTable(self, varType, varId, varContext):
        # Gets the SymbolTable from the current scope
        tempSymbolTable = self.scopeDictionary.get(self.currentScope).symbolTable

        if varId not in tempSymbolTable:
            tempSymbolTable[varId] = VarSymbolTableItem(varId, varType, self.currentScope, varContext)
        else:
            print("Variable already exists!")

        self.scopeDictionary.get(self.currentScope).symbolTable = tempSymbolTable

    # Grammar saves a struct variable as
    #   struct+ID
    # So we're adding a struct prefix to make it match the grammar. For example, struct "A" will be saved as "structA" in the struct dictionary.
    # This is so if we have a var saved with type structA, it will look it up directly instead of adding the prefix when searching.
    def addStructToSymbolTable(self, structId):
        structId = "struct"+structId
        if structId not in self.structDictionary:
            self.structDictionary[structId] = StructSymbolTableItem(structId=structId, structMembers={})

    def addVarToStruct(self, structId, varType, varId, varContext):
        structId = "struct"+structId
        tempStructMembers = self.structDictionary.get(structId).structMembers

        if varId not in tempStructMembers:
            tempStructMembers[varId] = VarSymbolTableItem(varId, varType, self.currentScope, varContext)
        else:
            print("Variable already exists!")

        self.structDictionary.get(structId).structMembers = tempStructMembers

    def lookupSymbolTableVar(self, varId):
        print("sim")

    def updateSymbolTableVar(self, varId, newValue):
        print("update")

    def emptySymbolTable():
        print("empty")

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
        print("     Items:", v.symbolTable)

    #for var, varItem in v.symbolTable.items():
    #print("         VAR: ", var)
    #print("         VarType: ", varItem.varType)

    print("--------------------------------------------")

    for c, v in printer.structDictionary.items():
        print("STRUCT: ", c)
        print("     Items: ", v.structMembers)

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

