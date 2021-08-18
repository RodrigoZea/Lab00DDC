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
    def __init__(self, varId, varType, scope):
        self.varId = varId 
        self.varType = varType
        self.scope = scope
        self.offset = 0

class MethodSymbolTableItem():
    def __init__(self, methodId, methodType):
        self.methodId = methodId
        self.methodType = methodType

# Comunicación: Scope de SymbolTableItem con MethodId de MethodSymbolTableItem

class StructSymbolTableItem():
    def __init__(self, varId, varType, structId):
        self.varId = varId 
        self.varType = varType
        self.structId = structId

# Comunicación: varType != primitivo en SymbolTableItem con structId de StructSymbolTableItem
    # Buscar en StructSymbolTable cada variable que le pertenece a la estructura

class SymbolTableItem():
    def __init__(self, parentKey, symbolTable, returnType):
        self.parentKey = parentKey,
        self.symbolTable = symbolTable,
        self.returnType = returnType

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

        super().__init__()

    def returnErrorList(self):
        return self.errorList

    def enterVarDeclaration(self, ctx: DecafParser.VarDeclarationContext):
        try:
            if (ctx.NUM() != None):
                value = ctx.getChild(3).getText()
                if (int(value) <= 0):
                    raise ArraySizeError
            else:
                # TODO: Add to symbol table!
                varType = ctx.getChild(0).getText()
                varId = ctx.getChild(1).getText()

                self.addToSymbolTable(varType, varId)

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


    def exitMethodDeclaration(self, ctx: DecafParser.MethodDeclarationContext):
        self.currentScope = "global"
        self.nestedCounter = 1
        return super().exitMethodDeclaration(ctx)

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

        return super().exitMethodDeclaration(ctx)

    def enterParameter(self, ctx: DecafParser.ParameterContext):
        paramType = ctx.getChild(0).getText()

        if paramType != 'void':
            paramId = ctx.getChild(1).getText()
            self.addToSymbolTable(paramType, paramId)

        return super().enterParameter(ctx)

    def enterScope(self, scope):
        self.pastScope = self.currentScope
        self.currentScope = scope

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

            self.lookupSymbolTableVar()

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
    """
    TODO: Rework symboltables to lists
    """

    def addToSymbolTable(self, varType, varId):
        # TODO: Change table from list to another dictionary to speedup computation time.
        # -------------------------------------------------------------------------------
        # Scope doesnt exist in dictionary
        if self.currentScope not in self.scopeDictionary:
            self.scopeDictionary[self.currentScope] = [VarSymbolTableItem(varId, varType)]
        # Scope already exists
        else:
            # Check if variable has already been declared in current scope
            exists = False
            for item in self.scopeDictionary[self.currentScope]:
                if item.varId == varId:
                    exists = True 

            if not exists:
                self.scopeDictionary[self.currentScope].append(VarSymbolTableItem(varId, varType))

    def addScopeToSymbolTable(self, pastScope, methodType=None):
        if self.currentScope not in self.scopeDictionary:
            self.scopeDictionary[self.currentScope] = SymbolTableItem(pastScope, {}, methodType)
        else:
            print("Scope name already exists!")

    # TODO: Save if its a parameter or not
    def addVarToSymbolTable(self, varType, varId):
        # Gets the SymbolTable from the current scope
        tempSymbolTable = self.scopeDictionary.get(self.currentScope).symbolTable

        if (tempSymbolTable):
            exists = False

            for keyVarId in tempSymbolTable:
                if (keyVarId == varId):
                    exists = True

            if not exists:
                tempSymbolTable[varId] = varType
            else:
                print("Variable already exists!")

        self.scopeDictionary.get(self.currentScope).symbolTable = tempSymbolTable

    # TODO: All :)
    def addStructToSymbolTable(self):
        print("struct")

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

        #print("VALUE: ", v)
        for a in v:
            print("     VALUE:", a.varType, a.varId)

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

