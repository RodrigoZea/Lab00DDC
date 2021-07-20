import sys
from antlr4 import *
from DecafLexer import DecafLexer
from DecafParser import DecafParser
from DecafListener import DecafListener

class KeyPrinter(DecafListener):
    def exitKey(self, ctx):
        print("Hello: %s" % ctx.ID())

def main(argv):
    #input_stream = FileStream(argv[1])
    lexer = DecafLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = DecafParser(stream)
    tree = parser.startRule()    

    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)

