import random

def random(state, player):
    return random.random()*5

def normal(state, player):
    return state.utility

def center(state, player):
    heuristic = 0
    for col in range(3, 6):
        for row in range(1, 7):
            if(state.board.get((col, row), None) == player):
                heuristic += 1
            elif(state.board.get((col, row), None) != player):
                heuristic -= 1

    final = heuristic + (random.random()-0.5)
    return final

def maxRows(state, player):
    maxInRows = 0
    for row in range(1, 7):
        maxInRow = 0
        for col in range(1, 8):
            if(state.board.get((col, row), None) == player):
                maxInRow += 1

        maxInRows = max(maxInRows, maxInRow);

    final = maxInRows + (random.random()-0.5)
<<<<<<< HEAD
    return final
=======
    return final


def lineWeight(state, initpos, direction, placedcellsmultiplier = 4):
    #placedcellsmultiplier= valor x defecto
    rows = 6
    cols = 7
    result = 0

    x, y = initpos
    dir_x, dir_y = direction

    while True:

        next_four_x = x + 3 *dir_x
        next_four_y = y + 3 *dir_y

        if next_four_x > cols or next_four_y > rows or next_four_x <= 0 or next_four_y <= 0:
            break


        last_placed = '.'
        placed = 0
        for delta in range(0, 4):
            delta_x = dir_x * delta
            delta_y = dir_y * delta
            actual_cell = state.board.get((y + delta_y, x + delta_x), '.')

            if last_placed == '.' and actual_cell != '.':
                last_placed = actual_cell

            if actual_cell != '.' and last_placed != actual_cell:
                last_placed = '.'
                break
            elif actual_cell != '.':# and last_placed == actual_cell:
                last_placed = actual_cell
                placed += 1


        if last_placed != '.':
            factor = 1 if last_placed == state.realPlayer else -1
            result += placedcellsmultiplier * placed * factor
        #avanzamos el trozo
        x += dir_x
        y += dir_y

    return result


def chachi(state, lineFunction = lineWeight):
    cols = 7
    rows = 6

    if state.utility != 0:
        factor = state.utility
        if state.realPlayer == 'O':
            factor *= -1

        return factor * 100000


    heuristic = 0
    # Check Horizontals
    for row in range(1,rows+1):
        #vertical
        heuristic += lineFunction(state, (1,row), (0,1))

    for row in range(1, 4):
        # Diagonal /
        heuristic += lineFunction(state, (1,row), (1, 1))
        heuristic += lineFunction(state, (row+1,1), (1, 1))

        # Diagonal \
        heuristic += lineFunction(state, (1, rows - row), (1, -1))
        heuristic += lineFunction(state, (row, cols), (1, -1))

    # Check Verticals
    for col in range(1,cols+1):
        heuristic += lineFunction(state, (col,1), (1,0))

    return heuristic + heuristic/5 * random.random()


def chachi_cutoff(state, depth):
    is_terminal_state = state.utility != 0 or len(state.moves) == 0
    if (depth == 0 or depth == 1) and state.utility != 0:
        state.utility *= 10000000
        return True;
    elif state.utility != 0:
        state.utility *= 10000
        return True;

    return depth > state.d or is_terminal_state


>>>>>>> 89c3886... Final
