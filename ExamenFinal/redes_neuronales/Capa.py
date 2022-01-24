from ExamenFinal.redes_neuronales.Neurona import *

class Capa:
    
    def __init__(self,entradas,pesos,sesgos):
        self.entradas = entradas
        self.pesos = pesos
        self.sesgos = sesgos
        
    def asignacion(self):
        for s in range(len(self.sesgos)):
            neuronas[s]= Neurona(self.entradas,self.pesos[s],self.sesgos[s])
        return neuronas                        
    def get_salidas(self):
        neuronas = asignacion()
        for i in range(len(self.sesgos)):
            neuronas[i].activacion()
        
    
    