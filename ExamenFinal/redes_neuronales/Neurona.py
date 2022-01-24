import math

class Neurona:
    
    def __init__(self, entradas,pesos,sesgo):
        self.entradas = entradas
        self.pesos = pesos
        self.sesgo = sesgo
        
    
    def sumatoria(self):
        a = 0
        for i in range(len(self.entradas)):
            y = self.weights[i]*self.entradas[i]
            print(f"\n{y}\n")
            a = a + y
            #print(f"\n{a}\n")
        return a + self.sesgo
    
    def activacion(self):
        a = self.sumatoria()
        print(f"\n{a}\n")
        a = math.e**(-a)
        print(f"\n{a}\n")
        a = 1 / ( 1 + a )
        return a
    
    
        
            