import re
import math
class Translator():
    def __init__(self, file, scopeSymTable, structSymTable):
        self.file = file
        self.currMethodSize = 0
        self.regDict = {}
        self.addrDict = {}
        self.instructionList = []
        self.paramList = []
        self.scopeSymbolTable = scopeSymTable
        self.structSymbolTable = structSymTable
        self.readFile()

    def readFile(self):
        f = open(self.file, "r")
        self.writeData()
        self.addLine(".text")
        self.createInstruction("la", "$s7", "G")
        self.createInstruction("j", "main")
        for x in f:
            #print(x)
            self.translateLine(x) 

    def writeData(self):
        self.addLine(".data")
        self.addLine(".align 2")
        globalVars = self.scopeSymbolTable.get("global").symbolTable
        totalGlobalVarsSize = 0

        for key, stVar in globalVars.items():
            totalGlobalVarsSize += stVar.size
            self.createData("G", "space", totalGlobalVarsSize)

        self.createData("newline", "asciiz", '"\n"')
        self.createData("intPrompt", "asciiz", "Ingrese un número entero: ")
        

    def translateLine(self, line):
        if line != "":
            # Label
            if ":" in line:
                if "InputInt" in line:
                    self.inputInt()
                elif "OutputInt" in line:
                    self.outputInt()
                elif "_exit" not in line:
                    self.addLine("  "+line.rstrip("\n"))
                    methodName = line[:-2]
                    if (methodName in self.scopeSymbolTable):
                        self.initializeRegisters()
                        methodSize = self.getMethodSize(methodName)
                        self.createAddrList(methodName)
                        # Allocate $ra space
                        self.createInstruction('sub', '$sp', '$sp', '4')
                        # ($sp) means we're accesing 0($sp) but the 0 isn't needed
                        self.createInstruction('sw', '$ra', '($sp)')
                        # Allocate "method space"
                        self.createInstruction('sub', '$fp', '$sp', methodSize)
                        self.createInstruction('la', '$sp', '($fp)')
                        self.currMethodSize = methodSize
                else:
                    self.createInstruction('add', '$sp', '$fp', self.currMethodSize)
                    self.createInstruction('lw', '$ra', '($sp)')
                    self.createInstruction('add', '$sp', '$sp', '4')
                    self.createInstruction('jr', '$ra')
            elif "param" in line:
                paramSplit = line.split()
                param = paramSplit[1]
                self.paramList.append(param)
            elif "call" in line:
                paramOffset = 8
                if (self.paramList != []):
                    for param in reversed(self.paramList):
                        if ("t" in param):
                            if param not in self.addrDict: self.addrDict[param] = []

                        paramReg = self.getReg([param])
                        reg = self.translateTemp(param)
                        if (reg != None):
                            regDest = self.getReg(param)
                            self.createInstruction("sw", "$"+regDest, '('+reg+')')

                        self.createInstruction("lw", "$"+paramReg[0], self.translateToSp(param))
                        self.createInstruction("sw", "$"+paramReg[0], "-"+str(paramOffset)+"($sp)")
                        paramOffset -= 4

                self.paramList = []
                # Call method
                callSplit = line.split()
                methodName = callSplit[1].split(',')[0]
                self.createInstruction('j', methodName)
            elif "if" in line:
                ifSplit = line.split()
                condition = ifSplit[1]
                goto = ifSplit[-1]

                opIndex = re.search('\>=|\<=|\>|\<|\==', condition)
                if (opIndex):
                    operator = condition[opIndex.start():opIndex.end()]
                    operands = condition.split(operator)
                    op1 = operands[0]
                    op2 = operands[1]
                    opTranslated = self.getBranchOperation(operator)

                    opList = [op1, op2]
                    regList = self.getReg(opList)

                    for op in opList: 
                        reg = self.translateTemp(op)
                        if (reg != None):
                            regDest = self.getReg(op)
                            self.createInstruction("sw", "$"+regDest, '('+reg+')')

                    if (len(regList) > 2):
                        self.saveMachineState()
                        self.createInstruction(opTranslated, '$'+regList[0], '$'+regList[1], goto)

            elif "goto" in line:
                gotoSplit = line.split()
                self.saveMachineState()
                self.createInstruction('j', gotoSplit[1])
            elif "=" in line:
                eqSplit = line.split("=")
                leftOp = eqSplit[0].strip()
                opIndex = re.search('\+|\-|\*|\/', eqSplit[1])
                if (opIndex):
                    # x = y + z
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

                    opList = [leftOp, op1, op2]
                    regList = self.getReg(opList)
                    
                    if (len(regList) > 2):
                        for op in opList: 
                            reg = self.translateTemp(op)
                            if (reg != None):
                                regDest = self.getReg(op)
                                self.createInstruction("sw", "$"+regDest, '('+reg+')')

                        self.createInstruction(opTranslated, '$'+regList[0], '$'+regList[1], '$'+regList[2])
                        self.handleOperation(regList[0], leftOp)

                        # If temp has been used on right side, free space
                        if ("t" in op1):
                            self.removeTemp(op1)
                        if ("t" in op2):
                            self.removeTemp(op2)
                else:
                    # x = y
                    op1 = eqSplit[1].rstrip("\n")

                    if ("t" in op1):
                        if op1 not in self.addrDict: self.addrDict[op1] = []
                    if ("t" in leftOp):
                        if leftOp not in self.addrDict: self.addrDict[leftOp] = []
                    
                    opList = [leftOp, op1]
                    regList = self.getReg(opList)

                    if (len(regList) > 1):
                        for op in opList: 
                            reg = self.translateTemp(op)
                            if (reg != None):
                                regDest = self.getReg(op)
                                self.createInstruction("sw", "$"+regDest, '('+reg+')')

                            regDest = self.getReg(op)
                            self.createInstruction("sw", "$"+regDest, '('+reg+')')

                        self.createInstruction("move", '$'+regList[0], '$'+regList[1])

                        if (regList[1] != "v0"):
                            self.handleCopy(regList[1], leftOp)

                        # If temp has been used on right side, free space
                        if ("t" in op1):
                            self.removeTemp(op1)
            elif "return" in line:
                wsSplit = line.split()
                op1 = wsSplit[1].rstrip("\n")
                print("operation: " + op1)
                regList = self.getReg([op1])
                self.createInstruction("move", '$v0', '$'+regList[0])
                #self.createInstruction("move", '$v0', '$temp')
   
    # Takes a String[] with the vars in order (left right var 1st, first var after the = is 2nd, var after operator is 3rd)
    def getReg(self, varList):
        regSelectedList = []
        for i in range(0, len(varList)): 
            stopSearch = False
            # Check if its a literal
            if (varList[i] not in self.addrDict):
                if (varList[i] == "R"):
                    regSelectedList.append("v0")
                else:
                    # If var is not in a register, but there is a register that is currently empty, pick it
                    for r, regList in self.regDict.items():
                        if (regList == []): 
                            regSelectedList.append(r)
                            stopSearch = True
                            # Check value to load
                            self.createInstruction('li', '$'+r, varList[i])
                        if (stopSearch): break 
            else:
                # If var is currently in a register, pick a register already containing it.
                for r, regList in self.regDict.items():
                    if varList[i] in regList: 
                        regSelectedList.append(r)
                        stopSearch = True
                    if (stopSearch): break 
                if (stopSearch): continue
                # If var is not in a register, but there is a register that is currently empty, pick it
                for r, regList in self.regDict.items():
                    if (regList == []): 
                        regSelectedList.append(r)
                        stopSearch = True
                        if ("t" not in varList[i]):
                            # Check value to load 
                            self.createInstruction('lw', '$'+r, self.translateToSp(varList[i]))
                            #L[0] -> 0($sp)
                            self.handleLoad(r, varList[i])
                    if (stopSearch): break  
                if (stopSearch): continue
                # Var is not in a register and there is no register that is currently empty
                # Possibility 2: Check if its not the variable on the left and its also the same one used to store the var 
                if (i > 0):
                    if varList[i] == varList[0]:
                        regSelectedList.append(regList[0])
                        stopSearch = True 
                if (stopSearch): continue
                # Spill
                score = [None, math.inf]
                for r, regList in self.regDict.items():
                    newScore = len(regList)
                    if (newScore < score[1]):
                        score = [r, newScore]
                regSelectedList.append(score[0])
                self.createInstruction('sw', '$'+score[0], self.translateToSp(varList[i]))
                self.handleStore(varList[i])
        return regSelectedList

    def removeTemp(self, temp):
        self.addrDict.pop(temp, None)

        for r, regList in self.regDict:
            if temp in regList: regList.remove(temp)

    def translateToSp(self, op):
        if '[' in op:
            # Handle G
            context = op[0]
            offset = op[2:-1]

            if (context == 'L'):
                if ("t" not in offset):
                    return offset+'($sp)'
            elif (context == 'G'):
                if ("t" not in offset):
                    return 'G+'+str(offset)
        else:
            if ("t" in op):
                return op

    def translateTemp(self, op):
        if '[' in op:
            # Handle G
            context = op[0]
            offset = op[2:-1]
            if (context == 'L'):
                if ("t" in offset):
                    reg = self.getReg([offset])
                    self.createInstruction("add", "$"+reg[0], "$"+reg[0], "$sp")
            elif (context == 'G'):
                if ("t" in offset):
                    reg = self.getReg([offset])
                    self.createInstruction("add", "$"+reg[0], "$"+reg[0], "$s7")
        
        return reg[0]

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

    def getBranchOperation(self, operator):
        if (operator == '>'):
            return 'bgt'
        if (operator == '<'):
            return 'blt'
        if (operator == '=='):
            return 'beqz'
        if (operator == '>='):
            return 'bge'
        if (operator == '<='):
            return 'ble'
        return 'unknown'

    def saveMachineState(self):
        for addr, addrList in self.addrDict:
            reg = None 
            if addrList != []:
                for ad in addrList:
                    if ("t" in ad):
                        reg = ad
            
            if (reg != None):
                self.createInstruction("sw", "$"+reg, self.translateToSp(addr))

    def inputInt(self):
        self.createInstruction("li", "$v0", 4)
        self.createInstruction("la", "$a0", "intPrompt")
        self.createSimpleInstruction("syscall")
        self.createInstruction("li", "$v0", 5)
        self.createSimpleInstruction("syscall")
        self.createInstruction("jr", "$ra")
    
    def outputInt(self):
        self.createInstruction("li", "$v0", 1)
        self.createSimpleInstruction("syscall")
        self.createInstruction("li", "$v0", 4)
        self.createInstruction("la", "$a0", "newline")
        self.createSimpleInstruction("syscall")
        self.createInstruction("jr", "$ra")

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
        self.regDict[regx] = [addrx] 
        self.addrDict[addrx] = [regx] 
        for k in self.addrDict.keys():
            addrList = self.addrDict.get(k)
            if addrx in addrList: addrList.remove(addrx)

    def initializeRegisters(self):
        # t0-t9 (temporales para calculos intermedios)
        self.createRegList("t", 9)

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

    def createInstruction(self, operation, arg1, arg2=None, arg3=None):
        if (arg3 != None):
            self.addLine("      {0} {1}, {2}, {3}".format(operation, arg1, arg2, arg3))
        elif (arg2 != None):
            self.addLine("      {0} {1}, {2}".format(operation, arg1, arg2))
        else:
            self.addLine("      {0} {1}".format(operation, arg1))

    def createSimpleInstruction(self, instruction):
        self.addLine("      {0} ".format(instruction))

    def createData(self, varName, varType, varSize):
        self.addLine("  {0}: .{1} {2}".format(varName, varType, varSize))

    def addLine(self, line):
        self.instructionList.append(line+'\n')

def translate(file, scopeSymTable, structSymTable):
    translator = Translator(file, scopeSymTable, structSymTable)
    return translator.instructionList
