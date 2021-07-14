def draw_board(board):
    print(board[1],'|',board[2],'|',board[3])
    print('---------')
    print(board[4],'|',board[5],'|',board[6])
    print('---------')
    print(board[7],'|',board[8],'|',board[9])
    print('\n')
def check_win(board):
    if (board[1] == board[2] and board[1] == board[3]):
        return True
    elif (board[4] == board[5] and board[4] == board[6]):
        return True
    elif (board[7] == board[8] and board[7] == board[9]):
        return True
    elif (board[1] == board[4] and board[1] == board[7]):
        return True
    elif (board[2] == board[5] and board[2] == board[8]):
        return True
    elif (board[3] == board[6] and board[3] == board[9]):
        return True
    elif (board[1] == board[5] and board[1] == board[9]):
        return True
    elif (board[7] == board[5] and board[7] == board[3]):
        return True
    else:
        return False
def check_tie(board):
    for num in range(1,10):
        if board[num] in range(1,10):
            return False
    return True
def check_who_won(board, letter):
    if board[1] == board[2] and board[1] == board[3] and board[1] == letter:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == letter):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == letter):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == letter):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == letter):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == letter):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == letter):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == letter):
        return True
    else:
        return False
def comp_move(board):
    best_score = -100
    best_move = 0
    for num in range(1,10):
        if board[num] in range(1,10):
            board[num] = 'X'
            score = minimax(board, False)
            board[num] = num
            if(score > best_score):
                best_score = score
                best_move = num
    return best_move
#minimax
def minimax(board, isMaximizing):
    if check_who_won(board, 'X'):
        return 1
    elif check_who_won(board, 'O'):
        return -1
    elif check_tie(board):
        return 0
    if isMaximizing:
        best_score = -100
        for num in range(1,10):
            if board[num] in range(1,10):
                board[num] = 'X'
                score = minimax(board, False)
                board[num] = num
                if (score > best_score):
                    best_score = score
        return best_score
    else:
        best_score = 100
        for num in range(1,10):
            if (board[num] in range(1,10)):
                board[num] = 'O'
                score = minimax(board, True)
                board[num] = num
                if (score < best_score):
                    best_score = score
        return best_score

board = [0,1,2,3,4,5,6,7,8,9]
computer_win = False
draw_board(board)

while not (check_win(board) or check_tie(board)):
    num = comp_move(board)
    board[num] = 'X'
    print('The computer placed an O in position', num)
    draw_board(board)
    if check_win(board) or check_tie(board):
        computer_win = True
        break
    print('Choose a number:  ')
    num = int(input())
    while not num in range(1, 10) or board[num] == 'X' or board[num] == 'O' :
        print('You must choose a valid number (1-9) that is not already taken:  ')
        num = int(input())
    board[num] = 'O'
    draw_board(board)


if check_win(board) and computer_win==True:
    print('Computer wins!')
elif check_win(board):
    print('Player wins!')
else:
    print("It's a tie!")