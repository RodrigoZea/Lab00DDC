class Translator():
    def __init__(self, file):
        self.file = file
        self.readFile()

    def readFile(self):
        f = open(self.file, "r")
        for x in f:
            self.translateLine(x) 

    def translateLine(self, line):
        if line != "":
            print(line)

    def getReg(self, varToGet):
        print("getReg")

def translate(file):
    translator = Translator(file)
