board = [['_','_','_'],['_','_','_'],['_','_','_']]

def player_1_Pick_X_or_O():       #This function lets the first player chose X or O and assigns O or X to the second player
    player1_XorO = -1

    while player1_XorO != (0 or 1):
        player1_XorO = input('Please choose X or O (1 for X, 0 for O: ')
        if int(player1_XorO) == 0:
            print('You Chose O')
            player2_XorO = 1
            return 'O'
            break
        elif int(player1_XorO) == 1:
            print('You Chose X')
            player2_XorO = 0
            return 'X'
            break
        else:
            print('You can only choose 0 or 1!')

def Player_1_mark_Board_O():     #This function ask player 1 to pick a place on the board, and mark O, and mark the board if this place is empty
    while True:
        row = int(input('Player 1, choose a row (0-2): '))
        column = int(input('Choose a column (0-2): '))
        if row <0 or row > 2 or column < 0 or column > 2:
            print("must be between 0-2")
            continue
        if board[row][column] == "_":
            board[row][column] = 'O'
            break
        else:
            print('place already marked! Chose a new spot!: ')
#    for i in board:
#        print(i)
    return board

def Player_1_mark_Board_X():     #This function ask player 1 to pick a place on the board, and mark X, and mark the board if this place is empty
    while True:
        row = int(input('Player 1, choose a row (0-2): '))
        column = int(input('Choose a column (0-2): '))
        if row <0 or row > 2 or column < 0 or column > 2:
            print("must be between 0-2")
            continue
        if board[row][column] == "_":
            board[row][column] = 'X'
            break
        else:
            print('place already marked! Chose a new spot!: ')
#    for i in board:
#        print(i)
    return board

def computer_mark_X():   #This func. lets the computer to play as player2 and randomly mark the board with X.
    while True:
        import random
        row = random.randint(0,2)
        column = random.randint(0,2)
        if board[row][column] == "_":
            board[row][column] = 'X'
            break
    for i in board:
        print(i)
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
    return board

def checkIfWOn(c):    #This function checks if X or O won
    if board[0].count(c) == 3 or board[1].count(c) == 3 or board[2].count(c) == 3:
        return True
        print(c + ' Had won the game!')

    elif (board[0][0] == c and board[1][0] == c and board[2][0] == c) or (board[0][1] == c and board[1][1] == c and board[2][1] == c) or (board[0][2] == c and board[1][2] == c and board[2][2] == c):
        return True
        print(c + ' Had won the game!')
    elif (board[0][0] == c and board[1][1] == c and board[2][2] == c) or (board[0][2] == c and board[1][0] == c and board[2][0] == c):
        return True
        print(c + ' Had won the game!')
    else:
        return False

while True:         #The game plays out - turn by turn
    if player_1_Pick_X_or_O() == 'X':   #if X begins
        Player_1_mark_Board_X()
        computer_mark_O()
        Player_1_mark_Board_X()
        computer_mark_O()

        Player_1_mark_Board_X()
        if checkIfWOn('X') == True:
            for i in board:
                print(i)
            print('Player 1 Had won the game!')
            break
        computer_mark_O()
        if checkIfWOn('O') == True:
            print('Player 2 Had won the game!')
            break
        Player_1_mark_Board_X()
        if checkIfWOn('X') == True:
            for i in board:
                print(i)
            print('Player 1 Had won the game!')
            break
        computer_mark_O()
        if checkIfWOn('O') == True:
            print('Player 2 Had won the game!')
            break
        Player_1_mark_Board_X()
        if checkIfWOn('X') == True:
            for i in board:
                print(i)
            print('Player 1 Had won the game!')
            break

        print("It's a draw! Nobody win!" )
        print("Would you like a new game?")
        break
    else:                           #if O begins
        Player_1_mark_Board_O()
        computer_mark_X()
        Player_1_mark_Board_O()
        computer_mark_X()

        Player_1_mark_Board_O()
        if checkIfWOn('O') == True:
            for i in board:
                print(i)
            print('Player 1 Had won the game!')
            break
        computer_mark_X()
        if checkIfWOn('X') == True:
            print('Player 2 Had won the game!')
            break
        Player_1_mark_Board_O()
        if checkIfWOn('O') == True:
            for i in board:
                print(i)
            print('Player 1 Had won the game!')
            break
        computer_mark_X()
        if checkIfWOn('X') == True:
            print('Player 2 Had won the game!')
            break
        Player_1_mark_Board_O()
        if checkIfWOn('O') == True:
            for i in board:
                print(i)
            print('Player 1 Had won the game!')
            break

        for i in board:
            print(i)
        print("It's a draw! Nobody win!" )
        print("Would you like a new game?")
        break
