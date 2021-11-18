import re
import math
class Translator():
    def __init__(self, file, scopeSymTable, structSymTable):
        self.file = file
        self.currMethodSize = 0
        self.regDict = {}
        self.addrDict = {}
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
                if "_exit" not in line:
                    self.addLine(line.rstrip("\n"))
                    methodName = line[:-2]
                    if (methodName in self.scopeSymbolTable):
                        methodSize = self.getMethodSize(methodName)
                        self.createAddrList(methodName)
                        print(self.addrDict.keys())
                        self.createInstruction('addi', '$sp', '$sp', "-"+methodSize)
                        self.currMethodSize = methodSize
                else:
                    self.createInstruction('lw', '$s0', '($sp)')
                    self.createInstruction('lw', '$ra', '($sp)')
                    self.createInstruction('addi', '$sp', '$sp', self.currMethodSize)
            elif "=" in line:
                eqSplit = line.split("=")
                leftOp = eqSplit[0].strip()
                opIndex = re.search('\+|\-|\*|\/', eqSplit[1])
                if (opIndex):
                    operator = eqSplit[1][opIndex.start()]
                    operands = eqSplit[1].split(operator)
                    op1 = operands[0]
                    op2 = operands[1].rstrip("\n")
                    opTranslated = self.getOperation(operator)

                    if ("t" in op1):
                        if op1 not in self.addrDict: self.addrDict[op1] = []
                    if ("t" in op2):
                        if op2 not in self.addrDict: self.addrDict[op2] = []
                    if ("t" in leftOp):
                        if leftOp not in self.addrDict: self.addrDict[leftOp] = []

                    regList = self.getReg([leftOp, op1, op2])
                    
                    if (len(regList) > 2):
                        self.createInstruction(opTranslated, regList[0], regList[1], regList[2])
                else:
                    op1 = eqSplit[1].rstrip("\n")

                    if ("t" in op1):
                        if op1 not in self.addrDict: self.addrDict[op1] = []
                    if ("t" in leftOp):
                        if leftOp not in self.addrDict: self.addrDict[leftOp] = []
                    
                    regList = self.getReg([leftOp, op1])
            
   
    # Takes a String[] with the vars in order (left right var 1st, first var after the = is 2nd, var after operator is 3rd)
    def getReg(self, varList):
        regSelectedList = []
        for i in range(0, len(varList)): 
            #print("VarReg: " + varList[i])
            stopSearch = False
            # Check if its a literal
            if (varList[i] not in self.addrDict):
                # If var is not in a register, but there is a register that is currently empty, pick it
                for r, regList in self.regDict.items():
                    if (regList == []): 
                        regSelectedList.append("$"+r)
                        #print("Appended on literal " + varList[i] + ", " + r)
                        stopSearch = True
                        # Check value to load
                        self.createInstruction('li', "$"+r, varList[i])
                    if (stopSearch): break 
            else:
                # If var is currently in a register, pick a register already containing it.
                for r, regList in self.regDict.items():
                    if varList[i] in regList: 
                        regSelectedList.append("$"+r)
                        #print("Appended on saved reg " + varList[i] + ", " + r)
                        stopSearch = True
                    if (stopSearch): break 
                if (stopSearch): continue
                # If var is not in a register, but there is a register that is currently empty, pick it
                for r, regList in self.regDict.items():
                    if (regList == []): 
                        regSelectedList.append("$"+r)
                        #print("Appended on free reg " + varList[i] + ", " + r)
                        stopSearch = True
                        # Check value to load TODO 
                        self.createInstruction('lw', "$"+r, varList[i])
                        self.handleLoad(r, varList[i])
                    if (stopSearch): break  
                if (stopSearch): continue
                # Var is not in a register and there is no register that is currently empty
                # Possibility 1: Check address descriptor for var
                addrList = self.addrDict.get(varList[i])
                if addrList != []:
                    tempReg = self.getRegFromAddrDescriptor(varList[i])
                    if (tempReg != None):
                        regSelectedList.append("$"+tempReg)
                        #print("Appended on addr desc " + varList[i] + ", " + tempReg)
                        stopSearch = True 
                if (stopSearch): continue  
                # Possibility 2: Check if its not the variable on the left and its also the same one used to store the var 
                if (i > 0):
                    if varList[i] == varList[0]:
                        regSelectedList.append("$"+regList[0])
                        #print("Same operand" + varList[i] + ", " + regList[0])
                        stopSearch = True 
                if (stopSearch): continue
                # Spill
                score = [None, math.inf]
                for r, regList in self.regDict.items():
                    newScore = len(regList)
                    if (newScore < score[1]):
                        score = [r, newScore]
                regSelectedList.append("$"+score[0])
                #print("Appended on spill " + varList[i] + ", " + score[0])
                self.createInstruction('sw', varList[i], "$"+score[0])
                self.handleStore(varList[i])
        #print("RegList: ", regSelectedList)
        #print("-------------------------------")
        return regSelectedList

    def getRegFromAddrDescriptor(self, addr):
        reg = None
        addrList = self.addrDict.get(addr)
        for addrInd in addrList:
            if ("t" in addrInd or "s" in addrInd or "a" in addrInd  or "v" in addrInd):
                reg = addrInd
                break

        return reg

    def getOperation(self, operator):
        if (operator == '+'):
            return 'add'
        if (operator == '-'):
            return 'sub'
        if (operator == '/'):
            return 'div'
        if (operator == '*'):
            return 'mul'
        return 'unknown'

    def handleLoad(self, reg, addr):
        self.regDict[reg] = [addr]
        addrList = self.addrDict.get(addr)
        if reg not in addrList: addrList.append(reg)
    
    def handleStore(self, addr):
        addrList = self.addrDict.get(addr)
        if addr not in addrList: addrList.append(addr)

    def handleCopy(self, reg, addr):
        regList = self.regDict.get(reg)
        if addr not in regList: regList.append(addr)
        self.addrDict[addr] = [reg]

    def handleOperation(self, regx, addrx):
        self.regDict[regx] = addrx 
        self.addrDict[addrx] = regx 

        for k in self.addrDict.keys():
            addrList = self.addrDict.get(k)
            if addrx in addrList: addrList.remove(addrx)

    def initializeRegisters(self):
        # t0-t9 (temporales para calculos intermedios)
        self.createRegList("t", 9)
        # s0-s7 (Saved registers where values are saved across subroutine calls. typically saved in stack)
        #self.createRegList("s", 9)
        # a0-a3 (para argumentos de subrutinas)
        #self.createRegList("a", 3)
        # v0-v1 (para returns)
        #self.createRegList("v", 1)

    # Create a list based on the register initial and the amount of registers to create
    def createRegList(self, letter, maxRegCount):
        for i in range(0, maxRegCount+1):
            currentReg = letter+str(i)
            self.regDict[currentReg] = []

    def createAddrList(self, methodName):
        self.addrDict = {}

        symbolTableGlobal = self.scopeSymbolTable.get("global").symbolTable
        for key, stVar in symbolTableGlobal.items():
            self.addrDict[stVar.memoryLoc] = []

        symbolTableMethod = self.scopeSymbolTable.get(methodName).symbolTable
        for key, stVar in symbolTableMethod.items():
            self.addrDict[stVar.memoryLoc] = []
        
        for k in self.scopeSymbolTable.keys():
            childMethod = self.scopeSymbolTable.get(k)
            if (childMethod.parentKey == methodName):
                for key, stVar in childMethod.symbolTable.items():
                    self.addrDict[stVar.memoryLoc] = []

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
