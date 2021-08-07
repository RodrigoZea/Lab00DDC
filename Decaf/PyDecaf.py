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
    def __init__(self, varId, varType, scope):
        self.varId = varId
        self.varType = varType
        self.size = 0
        self.scope = scope
        self.varContext = ""

class MethodSymbolTableItem():
    def __init__(self, methodId, methodType, startLine, endLine):
        self.methodId = methodId
        self.methodType = methodType
        self.startLine = startLine
        self.endLine = endLine

# Maybe a class to check struct?

#---------------------------------------------------------------------------------------------------

class DecafPrinter(DecafListener):
    def __init__(self) -> None:
        # Flags or misc
        self.errorList = []
        self.mainFound = False
        self.currentMethodVoid = False
        self.currentScope = "global"

        # Symbol table related
        self.symbolTableVar = []
        self.symbolTableMethod = []
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
                    # Add to symbol table
                    newVarStEntry = SymbolTableItem(
                                        varType,
                                        varId,
                                        self.currentScope
                                    )

                    self.addToSymbolTable(item=newVarStEntry)

                    return super().enterVarDeclaration(ctx)
        except ArraySizeError:
            print("ArraySizeError at line %d: Array size must be bigger than 0" % ctx.start.line)

    def enterMethodDeclaration(self, ctx: DecafParser.MethodDeclarationContext):
        methodType = ctx.getChild(0).getText()
        methodName = ctx.getChild(1).getText()

        if (methodType == 'void'):
            self.currentMethodVoid = True

        # Switch scope to method
        self.enterScope(methodName)

        # Add to method symbol table
        newMethodStEntry = MethodSymbolTableItem(
                            methodName,
                            methodType,
                            ctx.start.line,
                            ctx.stop.line
                        )

        self.addToMethodSymbolTable(item=newMethodStEntry)

        # Add params to symbol table

        return super().enterMethodDeclaration(ctx)

    def enterBlock(self, ctx: DecafParser.BlockContext):
        return super().enterBlock(ctx)

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
                if ctx.getChild(0).getText() != '':
                    raise ReturnNotEmpty
            else:
                if ctx.getChild(0).getText() == '':
                    raise ReturnEmpty

            self.currentMethodVoid = False

            return super().enterStatement(ctx)

        except ReturnMissing:
            print("Expected return statement on method")
        except ReturnEmpty:
            print("Missing return value on non-void method")
        except ReturnNotEmpty:
            print("Void type method should have an empty return")

    def enterScope(self, scope):
        self.currentScope = scope

    def addToSymbolTable(self, item: SymbolTableItem):
        try:
            if self.symbolTableVar.count == 0:
                self.symbolTableVar.append(item)
            else:
                exists = False
                for i in self.symbolTableVar:
                    if (item.varId == i.varId and item.scope == i.scope):
                        exists = True

                if not exists:
                    self.symbolTableVar.append(item)
                else:
                    raise ExistingItem
                    
        except ExistingItem:
            print("Symbol %s is already declared in the same context.", item.varId)

    def addToMethodSymbolTable(self, item: MethodSymbolTableItem):
        try:
            if self.symbolTableMethod.count == 0:
                self.symbolTableMethod.append(item)
            else:
                exists = False
                for i in self.symbolTableMethod:
                    if item.methodId == i.methodId:
                        exists = True

                if not exists:
                    self.symbolTableMethod.append(item)
                else:
                    raise ExistingItem
                    
        except ExistingItem:
            print("Method %s is already declared.", item.methodId)

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

