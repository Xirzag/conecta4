import games
import heuristics as h

def human_select(game, state):
    y = -1
    x = 0

    while True:
        try:
            col_str = raw_input("Movimiento: ")
            x = int(str(col_str).strip())

            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]
            if y == -1:
                print "Movimiento no valido, intentalo de nuevo."
            else:
                break
        except:
            print "No se introdujo un numero, intentalo de nuevo."

    return x, y

def select_mode(game):
    while True:
        player_sel = raw_input("1)Jugador o 2)maquina: ").strip()
        if player_sel == '1':
            return player(game, human_select, dict(), "Le toca mover!")

        elif player_sel == '2':
            #dificultad
            player_sel = raw_input("Dificultad 1)Facil o 2)Medio 3) Dificil (O heuristica): ").strip()
            try:
                player_sel = int(player_sel)
                if player_sel >= 1 and player_sel <= 3 :
                    #tenemos que pasarle la profundida, euristica...--> esto va en alphabeta_search, pero
                    #si see lo pasamos como parametros nos lo detecta como una llamada, asi que hacemos un
                    #diccionario
                    return player(game, games.alphabeta_search, dict(d=player_sel, eval_fn=h.chachi,
                                                                     cutoff_test=h.chachi_cutoff), "Pensando...")
                else:
                    print "Opcion erronea"
            except:

                try:
                    depth = int(raw_input("Profundidad?: ").strip())
                    return eval("player(game, games.alphabeta_search, dict(d=" + str(depth) + ", eval_fn=h." + player_sel +"), 'Jugando "+ player_sel +"')")
                except Exception, e:
                    print "Hubo un error: ", str(e)
        else:
            print "Opcion erronea"




class player:
    def __init__(self, game, onplay, args, message=''):
        self.args = args
        self.game = game
        #que tiene q hacer al jugar
        self.f = onplay
        self.msg = message

    def play(self, state):
        print self.msg
        move = self.f(game=self.game, state=state, **self.args)
        state = self.game.make_move(move, state)
        return state

