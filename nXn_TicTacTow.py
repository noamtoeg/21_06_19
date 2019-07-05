# 21_06_19
def createBoard():   # create a nXn board
    board = []
    rowBoard = []
    for i in  range(int(input('Print Board size (3,4,5 etc.): '))):
        rowBoard.append('_')
    for i in rowBoard:
        board.append(rowBoard)
    print((board))
counter = 1

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

def Player_mark_Board():
    while True:
        if counter % 2 == 1:
            row = int(input('Player 1, choose a row (0-2): ')
        else:
            row = int(input('Player 2, choose a row (0-2): ')
        column = int(input('Choose a column (0-2): '))
        if row < 0 or row > 2 or column < 0 or column > 2:
            print("must be between 0-2")
            continue
        if board[row][column] == "_":
            if counter % 2 == 1:
                board[row][column] = 'X'
                break
            else:
                board[row][column] = 'O'
                break
        else:
            print('place already marked! Chose a new spot!: ')
    #for i in board:
    #print(i)
    #return board
    #counter++
