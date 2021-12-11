"""
Date:       2021-12-09
Authors:    Jorge Luis Rodríguez Guzmán
File:       T2E1_test_list.py
Brief:      Este programa modifica el contenido de una lista
            e imprime los resultados de cada modificación
Score:      -
Versión:    0.0.1
Fixes:      -
"""
if __name__ == '__main__':
    MIXTURA = (5,)
    OMITIBLE = (2,)
    ACORDE_NUEVO = ('G°7°','CMaj7')
    progresion = ['Bm_7M','F7_9#','E7_9','F#9b/A#','C#°7','E°7°']
    print(f'La progresión Original es esta:\n {progresion}\n')
    # 1. Utilizar el metodo append
    progresion.append(ACORDE_NUEVO[0])
    print(f'Se agrega {ACORDE_NUEVO[0]} al final:\n'
          f'{progresion} \n')
    # 2. Utilizar el método insert
    progresion.insert(MIXTURA[0],ACORDE_NUEVO[1])
    print(f'Se inserta {ACORDE_NUEVO[1]}' 
          f' en la posición {MIXTURA[0]}: \n')    
    # 3. Utilizar el método pop
    omitido = progresion[OMITIBLE[0]]
    progresion.pop(OMITIBLE[0])
    print(f'Se omite {omitido}:\n {progresion} \n')
    # 4. Ordenar de la A a la Z
    progresion.sort()
    print(f'Se ordena de la A a la Z:\n{progresion}\n')
    # 5. Ordenar de la Z a la A
    progresion.sort(reverse=True)
    print(f'Se ordena de la Z a la A:\n{progresion}')        
    