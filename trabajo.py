import games
import heuristics as h

game = games.ConectaCuatro()
state = game.initial

<<<<<<< HEAD
player = game.to_move(state)

=======
player1 = select_mode(game)
player2 = select_mode(game)
>>>>>>> 89c3886... Final

mode = raw_input("Elige la dificultad: 1) Facil 2) Medio 3) Dificil")

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':

        while True:
            coor_str = raw_input("Movimiento y: ")
            try:
                y = int(coor_str)
                if y not in game.legal_moves(state):
                    print "Movimiento no valido, intentalo de nuevo."
                else:
                    break
            except ValueError:
                print "No se introdujo un numero, intentalo de nuevo."
        print "Thinking..."
        '''y = games.alphabeta_search(state, game, 2)'''

        state = game.make_move(y, state)
    else:
<<<<<<< HEAD
        print "Thinking..."
        if mode == 1:
            move = games.alphabeta_search(state, game, 3, eval_fn=h.random)
        elif mode == 2:
            move = games.alphabeta_search(state, game, 2, eval_fn=h.maxRows)
        else:
            move = games.alphabeta_search(state, game, 3, eval_fn=h.maxRows)
        state = game.make_move(move, state)
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        if len(state.moves) == 0:
            print 'empate'
        else:
            print "Ganador " + player
        break

    player = game.to_move(state)
=======
        state = player2.play(state)

    print "============================"


game.display(state)
if len(state.moves) == 0 and state.utility == 0:
    print '\nEmpate'
else:
    print "\nGanador " + game.not_to_move(state)



>>>>>>> 89c3886... Final
