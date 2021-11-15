import re
class Translator():
    def __init__(self, file, scopeSymTable, structSymTable):
        self.file = file
        self.regDict = {}
        self.instructionList = []
        self.scopeSymbolTable = scopeSymTable
        self.structSymbolTable = structSymTable
        self.readFile()

    def readFile(self):
        self.initializeRegisters()
        f = open(self.file, "r")
        self.writeData()
        for x in f:
            self.translateLine(x) 

    def writeData(self):
        self.addLine(".data")
        globalVars = self.scopeSymbolTable.get("global").symbolTable

        for key, stVar in globalVars.items():
            self.createData(stVar.varId, "word", stVar.size)

    def translateLine(self, line):
        if line != "":
            # Label
            if ":" in line:
                self.addLine("_"+line)
                methodName = line[:-2]

                if (methodName in self.scopeSymbolTable):
                    methodSize = self.getMethodSize(methodName)
                    self.createInstruction('addi', '$sp', '$sp', "-"+methodSize)
            elif "=" in line:
                eqSplit = line.split("=")
                print(eqSplit)
                #re.search("+", eqSplit[1]).start()

                
    def getReg(self, varToGet):
        print("getReg")

    def getOperation(operator):
        if (operator == '+'):
            return 'add'
        if (operator == '-'):
            return 'sub'
        if (operator == '/'):
            return 'div'
        if (operator == '*'):
            return 'mul'

        return 'unknown'

    def initializeRegisters(self):
        # t0-t9 (temporales para calculos intermedios)
        self.createRegList("t", 9)
        # s0-s7 (Saved registers where values are saved across subroutine calls. typically saved in stack)
        self.createRegList("s", 9)
        # a0-a3 (para argumentos de subrutinas)
        self.createRegList("a", 3)
        # v0-v1 (para returns)
        self.createRegList("v", 1)

    # Create a list based on the register initial and the amount of registers to create
    def createRegList(self, letter, maxRegCount):
        for i in range(0, maxRegCount+1):
            currentReg = letter+str(i)
            self.regDict[currentReg] = []

    # Calculate method size (for stack allocation)
    def getMethodSize(self, methodName):
        methodSize = 0

        # Get vars in root method
        rootMethodSymTable = self.scopeSymbolTable.get(methodName).symbolTable
        for key, stVar in rootMethodSymTable.items():
            methodSize += stVar.size

        # Check list and methods who have that methodName as parent (child methods)    
        for k in self.scopeSymbolTable.keys():
            childMethod = self.scopeSymbolTable.get(k)
            if (childMethod.parentKey == methodName):
                for key, stVar in childMethod.symbolTable.items():
                    methodSize += stVar.size
           
        return str(methodSize)

    def createInstruction(self, operation, arg1, arg2, arg3=None):
        if (arg3 != None):
            self.addLine("  {0} {1}, {2}, {3}".format(operation, arg1, arg2, arg3))
        else:
            self.addLine("  {0} {1}, {2}".format(operation, arg1, arg2))

    def createData(self, varName, varType, varSize):
        self.addLine("  {0}: .{1} {2}".format(varName, varType, varSize))

    def addLine(self, line):
        self.instructionList.append(line)

def translate(file, scopeSymTable, structSymTable):
    translator = Translator(file, scopeSymTable, structSymTable)

    for line in translator.instructionList:
        print(line)
