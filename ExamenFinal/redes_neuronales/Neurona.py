import math

class Neurona:
    
    def __init__(self,entradas,pesos,sesgo):
        self.entradas = entradas
        self.pesos = pesos
        self.sesgo = sesgo
        
    
    def sumatoria(self):
        a = 0.0
        for i in range(len(self.entradas)):
            a = a + self.pesos[i]*self.entradas[i]
        return a + self.sesgo
    
    def activacion(self):
        a = self.sumatoria()
        a = math.e**(-a)
        a = 1 / ( 1 + a )
        return a
    
    
        
            