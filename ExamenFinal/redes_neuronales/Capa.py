from ExamenFinal.redes_neuronales.perceptron1 import *
class Capa:
    def __init__(self,entradas,neuronas,salidas):
        self.entradas = entradas
        self.neuronas = neuronas
        self.salidas = salidas 
        
    def asignacion(self):
        for n in neuronas:
            neuronas[n].inputs = Perceptron1(entradas,pesos,sesgos)
        
    