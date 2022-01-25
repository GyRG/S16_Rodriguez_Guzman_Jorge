from ExamenFinal.redes_neuronales.Neurona import *

class Capa:
    
    def __init__(self,entradas,pesos,sesgos):
        self.entradas = entradas
        self.pesos = pesos
        self.sesgos = sesgos
        self.neuronas = self.inicializar_neuronas()
        self.salidas = self.activacion_neuronas()
        
        
    def inicializar_neuronas(self):
        neuronas=[]
        for i in range(len(self.sesgos)):
            neuronas.append(
                Neurona(
                    self.entradas,
                    self.pesos[i],
                    self.sesgos[i])
                )
        return neuronas
                        
    def activacion_neuronas(self):
        salidas = []
        for i in range(len(self.sesgos)):
            salidas.append(
                self.neuronas[i].activacion()
                )
        return salidas
        
    
    