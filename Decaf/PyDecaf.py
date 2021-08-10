import sys
from antlr4 import *
from antlr4.tree.Trees import  TerminalNode
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.ErrorStrategy import ErrorStrategy, DefaultErrorStrategy
from antlr4.error.Errors import *
from DecafLexer import DecafLexer
from DecafParser import DecafParser
from DecafListener import DecafListener
from DecafErrors import *

class SymbolTableItem():
    def __init__(self, varId, varType):
        self.varId = varId 
        self.varType = varType

class MethodSymbolTableItem():
    def __init__(self, methodId, methodType):
        self.methodId = methodId
        self.methodType = methodType

# Maybe a class to check struct?
"""
class StructSymbolTableItem():
    def __init__(self):
        self.structId = structId
        self.size = 0

When adding to symbol table check if type is different from primitives, if it is, check on StructSymbolTable to see if its a valid name.

"""

#---------------------------------------------------------------------------------------------------

class DecafPrinter(DecafListener):
    def __init__(self) -> None:
        # Flags or misc
        self.errorList = []
        self.mainFound = False
        self.currentMethodVoid = False
        self.parentScope = None
        self.primitives = ('int', 'char', 'boolean', 'struct', 'void')

        # Symbol table related
        self.currentMethodName = ""
        self.currentScope = "global"
        self.nestedCounter = 1
        self.scopeDictionary = {}

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

        if (methodType == 'void'):
            self.currentMethodVoid = True

        self.currentMethodName = methodName
        self.enterScope(methodName)

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
        
        return super().enterBlock(ctx)
    
    def exitMethodDeclaration(self, ctx: DecafParser.MethodDeclarationContext):
        self.nestedCounter = 1

        return super().exitMethodDeclaration(ctx)

    def enterParameter(self, ctx: DecafParser.ParameterContext):
        paramType = ctx.getChild(0).getText()

        if paramType != 'void':
            paramId = ctx.getChild(1).getText()
            self.addToSymbolTable(paramType, paramId)

        return super().enterParameter(ctx)

    def enterScope(self, scope):
        self.currentScope = scope

    def addToSymbolTable(self, varType, varId):
        # Scope doesnt exist in dictionary
        if self.currentScope not in self.scopeDictionary:
            self.scopeDictionary[self.currentScope] = [SymbolTableItem(varId, varType)]
        # Scope already exists
        else:
            # Check if variable has already been declared in current scope
            exists = False
            for item in self.scopeDictionary[self.currentScope]:
                if item.varId == varId:
                    exists = True 

            if not exists:
                self.scopeDictionary[self.currentScope].append(SymbolTableItem(varId, varType))

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

            if self.currentMethodVoid:
                if ctx.getChild(0).getText() == "return" and ctx.getChild(1).getText() != '':
                    raise ReturnNotEmpty
            else:
                if ctx.getChild(1).getText() == '':
                    raise ReturnEmpty

            self.currentMethodVoid = False

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

