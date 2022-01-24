import math

class Capa:
    
    def __init__(self, inputs,weights,bias):
        self.inputs = inputs
        self.weights = weights
        self.bias = bias
        
    
    def sumatoria(self):
        a = 0
        for i in range(len(self.inputs)):
            y = self.weights[i]*self.inputs[i]
            print(f"\n{y}\n")
            a = a + y
            #print(f"\n{a}\n")
        return a + self.bias
    
    def activacion(self):
        a = self.sumatoria()
        print(f"\n{a}\n")
        a = math.e**(-a)
        print(f"\n{a}\n")
        a = 1 / ( 1 + a )
        return a
    
    
        
            