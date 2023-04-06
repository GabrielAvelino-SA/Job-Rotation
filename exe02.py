class fibonacci:
    def __init__(self, antesessor, suscessor):
        self.antecessor = antesessor
        self.suscessor = suscessor

    def getAntecessor(self):
        return self.antecessor
    def getSuscessor(self):
        return self.suscessor
    
    def append(self):
        acumulador = self.getAntecessor()
        self.antecessor = self.getSuscessor()
        self.suscessor = self.suscessor + acumulador

nun = int (input (""))

Fibonacci = fibonacci(0,1)

while (nun > Fibonacci.getSuscessor()):
    Fibonacci.append()
    print (f"[{Fibonacci.antecessor},{Fibonacci.suscessor}]")

if (nun == Fibonacci.getSuscessor()):
    print("o número informado pertence a sequência")
else:
    print("o número informado não pertence a sequência")