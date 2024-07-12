import random


# Takes values array as input to check for best possible placement for computer player, otherwise random. '\x19' == empty space unicode as hex.
def findWinningMove(values):
    #OHorizontal
    for i in range(0, 9, 3):
        if values[i] == 'O' and values[i+1] == 'O' and (values[i+2] == '\x19'):
            return i+2
        elif values[i] == 'O' and values[i+2] == 'O' and (values[i+1] == '\x19'):
            return i+1
        elif values[i+1] == 'X' and values[i+2] == 'X' and (values[i] == '\x19'):
            return i
    #OVertical
    for i in range(3):
        if values[i] == 'O' and values[i+3] == 'O' and (values[i+6] == '\x19'):
            return i+6
        elif values[i] == 'O' and values[i+6] == 'O' and (values[i+3] == '\x19'):
            return i+3
        elif values[i+3] == 'O' and values[i+6] == 'O' and (values[i] == '\x19'):
            return i
    #ODiagonal
    if values[0] == 'O' and values[4] == 'O' and (values[8] == '\x19'):
        return 8
    elif values[0] == 'O' and values[8] == 'O' and (values[4] == '\x19'):
        return 4
    elif values[4] == 'O' and values[8] == 'O' and (values[0] == '\x19'):
        return 0
    elif values[2] == 'O' and values[4] == 'O' and (values[6] == '\x19'):
        return 6
    elif values[2] == 'O' and values[6] == 'O' and (values[4] == '\x19'):
        return 4
    elif values[4] == 'O' and values[6] == 'O' and (values[2] == '\x19'):
        return 2
    #XHorizontal
    for i in range(0, 9, 3):
        if values[i] == 'X' and values[i+1] == 'X' and (values[i+2] == '\x19'):
            return i+2
        elif values[i] == 'X' and values[i+2] == 'X' and (values[i+1] == '\x19'):
            return i+1
        elif values[i+1] == 'X' and values[i+2] == 'X' and (values[i] == '\x19'):
            return i
    #XVerticle
    for i in range(3):
        if values[i] == 'X' and values[i+3] == 'X' and (values[i+6] == '\x19'):
            return i+6
        elif values[i] == 'X' and values[i+6] == 'X' and (values[i+3] == '\x19'):
            return i+3
        elif values[i+3] == 'X' and values[i+6] == 'X' and (values[i] == '\x19'):
            return i
    #XDiagonal
    if values[0] == 'X' and values[4] == 'X' and (values[8] == '\x19'):
        return 8
    elif values[0] == 'X' and values[8] == 'X' and (values[4] == '\x19'):
        return 4
    elif values[4] == 'X' and values[8] == 'X' and (values[0] == '\x19'):
        return 0
    elif values[2] == 'X' and values[4] == 'X' and (values[6] == '\x19'):
        return 6
    elif values[2] == 'X' and values[6] == 'X' and (values[4] == '\x19'):
        return 4
    elif values[4] == 'X' and values[6] == 'X' and (values[2] == '\x19'):
        return 2
    if values[4] == '\x19':
        return 4
    else:
        empty = []
        for i in range(9):
            if values[i] == '\x19':
                empty.append(i)
        if (len(empty)-1) > 0:
            return empty[random.randint(0, (len(empty)-1),)]
        else:
            return "tie"

# Checks if either X's or O's have won or for a tie
def isWin(values):
    # horizontal win
    for i in range(0, 9, 3):
        if values[i] == 'X' and values[i+1] == 'X' and values[i+2] == 'X':
            return 'X'
        elif values[i] == 'O' and values[i+1] == 'O' and values[i+2] == 'O':
            return 'O'
    # Verticle win
    for i in range(3):
        if values[i] == 'X' and values[i+3] == 'X' and values[i+6] == 'X':
            return 'X'
        elif values[i] == 'O' and values[i+3] == 'O' and values[i+6] == 'O':
            return 'O'
    # Diagonal win
    if (values[0] == 'X' and values[4] == 'X' and values[8] == 'X'):
        return 'X'
    elif((values[0] == 'O' and values[4] == 'O' and values[8] == 'O')):
        return 'O'
    elif (values[2] == 'X' and values[4] == 'X' and values[6] == 'X'):
        return 'X'
    elif (values[2] == 'O' and values[4] == 'O' and values[6] == 'O'):
        return 'O'
    # Tied
    empty = []
    for i in range(9):
        if values[i] == '\x19':
            empty.append(i)
    if len(empty) == 0:
        return 'tie'