# conecta4

Permite jugar contra una IA al cuatro en raya o conecta 4.

Puedes seleccionar dificultad de la IA y quien va a jugar esa partida. Esta basado en el código 
https://github.com/cayetanoguerra/fsi/tree/master/Week%204%20-%20Conecta%204

La inteligencia artificial funciona con un algoritmo minimax con poda alfabeta, que utiliza una heuristica cuando llega a una determinada profundidad. Esta profundidad esta determinada por el nivel de dificultad.
La heuristica comprueba todas las posibles posiciones donde se puede hacer 4 en raya y va sumando las fichas que hay en ellas si es posible hacer el 4 en raya.

También puedes usar tu propia heuristica, añadirla al fichero heuristics y llamarla desde el menu del juego.
