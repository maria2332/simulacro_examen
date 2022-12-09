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

# Definimos una función que tome una cadena de caracteres y devuelva un diccionario con las subcadenas y su puntuación
def minion_game(string):
  # Creamos un diccionario vacío que almacenará las subcadenas y su puntuación
  substrings = {}
  # Iteramos sobre todas las letras de la cadena
  for i in range(len(string)):
    # Stuart forma palabras que comiencen con consonantes
    if string[i] not in "AEIOU":
      # Iteramos sobre todas las subcadenas que comiencen con la letra actual
      for j in range(i + 1, len(string) + 1):
        # Agregamos la subcadena al diccionario y aumentamos su puntuación en 1
        substrings[string[i:j]] = substrings.get(string[i:j], 0) + 1
        
    # Kevin forma palabras que comiencen con vocales
    else:
      # Iteramos sobre todas las subcadenas que comiencen con la letra actual
      for j in range(i + 1, len(string) + 1):
        # Agregamos la subcadena al diccionario y aumentamos su puntuación en 1
        substrings[string[i:j]] = substrings.get(string[i:j], 0) + 1
  return substrings
# Probamos la función con la cadena "BANANA"
print(minion_game("BANANA"))
# Deberíamos obtener el siguiente diccionario como resultado:
# {
#   "B": 1,
#   "BA": 1,
#   "BAN": 1,
#   "BANA": 1,
#   "AN": 2,
#   "ANA": 2,
#   "N": 2,
#   "NA": 2,
#   "A": 3
# }
