from modes import *

game = games.ConnectFour()
state = game.initial

player1 = select_mode(game)
player2 = select_mode(game)

startToken = game.to_move(state)

while not game.terminal_test(state):
    game.display(state)
    print "\n\nJugador a mover:", game.to_move(state)

    if game.to_move(state) == startToken:
        state = player1.play(state)

    else:
        state = player2.play(state)

    print "============================"


game.display(state)
if len(state.moves) == 0 and state.utility == 0:
    print '\nEmpate'
else:
    print "\nGanador " + game.not_to_move(state)



