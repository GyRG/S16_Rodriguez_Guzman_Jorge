# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 21:46:50 2021

@author: gyorg
"""
print("Hola Mundo")

userLoginCount = 5
print(userLoginCount)

print("Cambia imagen a escala de grises")

if __name__ == '__main__':
    contador = 6
    print('PyCharm')
    print ("sangría ")
    
    if(contador == 6):
        print("Contador vale 6")
    else:
        entrada = int(input("Ingresa un valor: "))
        print(entrada)
        print(type(entrada))
        
print("Hello","world","from","python",sep= ' ')

print(f'Libros: {3:d}\nPrice: ${12.375:f}\ntotal:{3*12.375:10.2f}')

print(f'Libros: {3:+d}\nPrice: ${12.375:-.2f}\ntotal:{3*12.375:010.4f}')

#%
print("Hola sección")

""" 
Hola este es un comentario 
de múltiples lineas
"""
def saludar(): 
    """esta función saluda desde mi casa  :return: dirección """
    print("Hola desde mi casa")
    
saludar()


i = 1
while i <= 6: 
    print(i)
    i+=1
    #i = i + .1
    if i==4:
        break
    
    