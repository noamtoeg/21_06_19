board = [['_','_','_'],['_','_','_'],['_','_','_']]

def computer_mark_X():   #This func. lets the computer to play as player1 and randomly mark the board with X.
    while True:
        import random
        row = random.randint(0,2)
        column = random.randint(0,2)
        if board[row][column] == "_":
            board[row][column] = 'X'
            break
#    for i in board:
#        print(i)
    return board

def computer_mark_O():  # This func. lets the computer to play as player2 and randomly mark the board with O.
    while True:
        import random
        row = random.randint(0,2)
        column = random.randint(0,2)
        if board[row][column] == "_":
            board[row][column] = 'O'
            break   #
    for i in board:
        print(i)
    print('---------------')
    return board

def checkIfWOn(c):    #This function checks if X or O won
    if board[0].count(c) == 3 or board[1].count(c) == 3 or board[2].count(c) == 3:
        return True

    elif (board[0][0] == c and board[1][0] == c and board[2][0] == c) or (board[0][1] == c and board[1][1] == c and board[2][1] == c) or (board[0][2] == c and board[1][2] == c and board[2][2] == c):
        return True
    elif (board[0][0] == c and board[1][1] == c and board[2][2] == c) or (board[0][2] == c and board[1][1] == c and board[2][0] == c):
        return True
    else:
        return False

while True:         #The game plays out - turn by turn
        computer_mark_X()
        computer_mark_O()
        computer_mark_X()
        computer_mark_O()

        computer_mark_X()
        if checkIfWOn('X') == True:
            for i in board:
                print(i)
            print('Player 1 Had won the game!')
            break
        computer_mark_O()
        if checkIfWOn('O') == True:
            print('Player 2 Had won the game!')
            break
        computer_mark_X()
        if checkIfWOn('X') == True:
            for i in board:
                print(i)
            print('Player 1 Had won the game!')
            break
        computer_mark_O()
        if checkIfWOn('O') == True:
            print('Player 2 Had won the game!')
            break
        computer_mark_X()
        if checkIfWOn('X') == True:
            for i in board:
                print(i)
            print('Player 1 Had won the game!')
            break
        else:
            for i in board:
                print(i)

        print("It's a draw! Nobody win!" )
        print("Would you like a new game?")
        break
