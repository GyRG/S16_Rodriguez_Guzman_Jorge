"""
Date:       2022-01-23
Authors:    Jorge Luis Rodríguez Guzmán
File:       perceptron.py
Brief:      Este es el código con el que se resuelven
            los ejercicios 3, 4 y 5 del examen
            
Score:      -
Versión:    0.0.1
Fixes:      -
"""

from ExamenFinal.redes_neuronales.Neurona import *
from ExamenFinal.redes_neuronales.Capa import *


if __name__ == "__main__":
    entradas = [7,21,-10]
    pesos = [-2,4.5,8.2]
    sesgo = 0.5
        
    #ejercicio1 = Neurona(entradas,pesos,sesgo)
    
    #print(ejercicio1.activacion())
    
    entradas_2 = [0.1,0.5]
    pesos_2 = [[-4.8,4.6],[5.1,-5.2]]
    sesgos_2 = [-2.6,3.2,-1.3]
    ejercicio2 = Capa(entradas_2,pesos_2,sesgos_2)
    
    