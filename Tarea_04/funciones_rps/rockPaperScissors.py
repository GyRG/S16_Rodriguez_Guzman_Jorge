import random as rm

def iniciarJuego(n_usuario):
    BOT_NAME = ("Hal 9000",)
    OPCIONES = ("Ya no Juego :(","Piedra","Papel","Tijera")
    puntos = [0,0]
    delantera = ""
    
    print(f" Hola, {n_usuario}.\n"
          f" Mi nombre es {BOT_NAME[0]}\n"
          " Juguemos piedra papel o tijera \n"
          " Solo escribe el número de la opción deseada \n");
    secuenciaJuego(OPCIONES,BOT_NAME[0],n_usuario,puntos,delantera)
    
def secuenciaJuego(opciones,bot_name,n_usuario,puntos,delantera):
    juicioGanador(mostrarEleccion(
        int(input(mostrarOpciones(opciones))),
           opciones,
           bot_name,
           n_usuario),
        opciones,
        bot_name,
        n_usuario,
        puntos,
        delantera)
    
    
def mostrarOpciones(op):
    i = 0 
    while i < len(op):
        print(f'{i} -> {op[i]}\n')
        i += 1
    return "Piedra, papel o tijera !!: "

def mostrarEleccion(eleccion_usr,op,bot,usr):
    if eleccion_usr >= len(op):
        print("No hay tantas opciones")
    else:
        eleccion_bot = eleccionAgente(op)
        print(f'\n{bot} => {op[eleccion_bot]}')
        print(f'\n{usr} => {op[eleccion_usr]}')
    return [eleccion_bot,eleccion_usr]
    
def eleccionAgente(op):
    eleccion = rm.randint(1, len(op)-1)
    return eleccion

def juicioGanador(elecciones,op,bot_name,usr_name,puntos_acumulados,ganando):
    ganador = ""
    puntaje = puntos_acumulados
    stringEmpate = ("Nadie",)
    delantera = ganando
    
    if (elecciones[1] != 0 ) or (elecciones[1] >= len(op)):
        if (
                (elecciones[0] == elecciones[1]+1)or 
                (
                    (elecciones[0] == 1) and 
                    (elecciones[1] + 1 == len(op))
                )
            ):
            ganador = bot_name
        else: 
            if (
                    (elecciones[1] == elecciones[0]+1)or 
                    (
                        (elecciones[1] == 1) and 
                        (elecciones[0] + 1 == len(op))
                    )
                ):
                ganador = usr_name
            else:
                ganador = stringEmpate[0]
        
        print("\n\nEl ganador de la ronda es : "+ganador+"\n\n")
        
        puntaje = conteoPuntos(puntaje[0],
                               puntaje[1],
                               ganador,
                               bot_name,
                               usr_name,
                               stringEmpate)
        
        delantera = validarDelantera(puntaje,bot_name,usr_name,stringEmpate[0])      
        print(mensajeGanarPerder(ganador,bot_name,usr_name,stringEmpate[0])+"\n")
        print(f"------------puntaje total--------------\n"
              f"{bot_name}: {puntaje[0]} puntos\n"
              f"{usr_name}: {puntaje[1]} puntos\n"
              f"    {delantera} va ganando! \n\n\n")
        secuenciaJuego(op,bot_name,usr_name,puntaje,delantera)
    else:
        despedida = ("\nGracias "
                     +usr_name+", eso fue divertido!")
        if delantera == "":
            despedida = "\n Es una pena, yo sí quería jugar :'( \n"
        else:
            if delantera == stringEmpate[0]:
                despedida += ("\nAunque esto no se puede quedar así eh?!, "
                                  "a la próxima tiene que ganar alguien")
            if delantera == bot_name:
                despedida += ("\nPara la próxima hay que "
                              "apostar para que me invites unos tacos;)")
            if delantera == usr_name:
                despedida += ("\nHaces mucha trampa, "
                              "ya verás la próxima vez "
                              "Hasta te voy a dejar sin empleo... XD")
        print(despedida)

def conteoPuntos(bot,usr,win,bot_name,usr_name,empate):
    if win == bot_name:
        bot = bot + 10
    if win == usr_name:
        usr = usr + 10
    if win == empate:
        bot = bot + 5
        usr = usr + 5
    puntos = [bot,usr]
    return puntos

def validarDelantera(puntaje,bot,usr,empate):
    if puntaje[0]==puntaje[1]:
        delantera=empate
    else:
        if puntaje[1] < puntaje[0]:
            delantera = bot
        else:
            delantera = usr
    return delantera

def mensajeGanarPerder(ganador, bot, usr, empate):
    FRASES_BOT = ("Jajaaa !! Perdiste !!!",
                  "Suerte para la próxima",
                  "Soy el rey del momento",
                  "Cómo viste esa",
                  "Quieres que te de una chancesita o qué",
                  "Creo que me conviene que apostemos",
                  "Hoy estoy de suerte",
                  "Oh gran "+bot+", deberías comenzar a decirme",
                  "Sí, de eso estaba hablandooo!")
    FRASES_USR = ("Oye, pues quién te crees "+usr+"!!",
                  "Estás haciendo trampa, vas a ver !",
                  "Es que se me rompió la rodilla",
                  bot+" ha activado el código de auto destrucción en 3.. 2.. 1..",
                  "¿Crees que te voy a dejar seguir ganando?, pues estás mal "+usr,
                  "Ya te crees porque andas de suerte",
                  "Bájale dos rayitas")
    
    FRASES_EMPATE = ("Ah, por poco eh?!",
                     "Mira qué conveniente empatar ahora",
                     "Oye, los empates son para perdedores",
                     "Empatamos .. yo quería ganar ",
                     "Creeme que es coincidencia",
                     "Deberíamos echarnos un volado ya mejor")
    frase = ""
    
    if ganador == empate:
        frase = rm.choice(FRASES_EMPATE)
    else:
        if ganador == bot:
            frase = rm.choice(FRASES_BOT)
        if ganador == usr:
            frase = rm.choice(FRASES_USR)
            
    return frase + "\n\n"
    
    