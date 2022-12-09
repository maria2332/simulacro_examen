"""
Reglas del juego
Ambos jugadores reciben la misma cadena de caracteres
Ambos jugadores tienen que hacer subcadenas usando las letras de la cadena
Stuart tiene que formar palabras que comiencen con consonantes .
Kevin tiene que formar palabras que comiencen con vocales .
El juego termina cuando ambos jugadores han creado todas las subcadenas posibles.
Puntuación
Un jugador obtiene un +1punto por cada aparición de la subcadena en la cadena.
Por ejemplo :
String= BANANA
Palabra inicial de la vocal de Kevin = ANA
Aquí, ANA aparece dos veces en BANANA . Por lo tanto, Kevin obtendrá 2 puntos.
Tu tarea es determinar el ganador del juego y su puntuación. El nombre y la puntuación del ganador, separados por un espacio en una línea, 
o Draw si no hay ningún ganador.
"""

from ast import main

def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        if [i] in vowels:
            kevin_score += (len(string)-i)
        else:
            stuart_score += (len(string)-i)
    if kevin_score > stuart_score:
        print ("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print ("Stuart", stuart_score)
    else:
        print ("Draw")

minion_game("BANANA")

if kevin_word == startswith("AEIOU")


if __name__ == '__main__':   
    main()