import random as rm

bot_name = ("Hal 9000",)
opciones = ("Terminar Juego","Piedra","Papel","Tijera")
def iniciarJuego(nombre):
    
    n = nombre
    print(f" Hola, {n}.\n"
          f" Mi nombre es {bot_name[0]}\n"
          " Juguemos piedra papel o tijera \n"
          " escriba el número de la opción deseada \n");
    juicio(input(mostrarOpciones(opciones)))
    
    
def mostrarOpciones(op):
    i = 0 
    while i < len(op):
        print(f'{op[i]}  = >  {i}\n')
        i += 1

def juicio(eleccion):
    print("eleccion")
    
def eleccionAgente(op):
    eleccion = rm.choice(op)
    return eleccion