from random import randint
def draw_board(board):
    print(board[0][0],'|',board[0][1],'|',board[0][2])
    print('---------')
    print(board[1][0],'|',board[1][1],'|',board[1][2])
    print('---------')
    print(board[2][0],'|',board[2][1],'|',board[2][2])
    print('\n')
def check_win(board):
    for x in range(3):
        if(board[x][0]==board[x][1]==board[x][2] or board[0][x]==board[1][x]==board[2][x]):
            return True
    return(board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0])
def check_tie(board):
    for x in range(49, 58):
        if chr(x) in board[0] or chr(x) in board[1] or chr(x) in board[2]:
            return False
    return True
def comp_move(board, filled):
    unfilled = []
    for x in range(1,10):
        if not x in filled:
            unfilled.append(x)
    x = randint(0, len(unfilled)-1)
    return unfilled[x]

board = [['1','2','3'],['4','5','6'],['7','8','9']]
player_win = False
draw_board(board)
filled = []
while not (check_win(board) or check_tie(board)):
    print('Choose a number:  ')
    num = input()
    while num in filled or not (len(num) == 1 and num != "0") or ord(num)-48>9 or ord(num)-48<1 or ord(num)-48 in filled:
        print('You must choose a valid number (1-9) that is not already taken:  ')
        num = input()
    num2 = ord(num) - 48
    filled.append(num)
    filled.append(num2)
    board[(num2-1)//3][(num2-1)%3] = 'X'
    draw_board(board)
    if check_win(board) or check_tie(board):
        player_win = True
        break
    num = comp_move(board, filled)
    filled.append(num)
    board[(num - 1) // 3][(num - 1) % 3] = 'O'
    print('The computer placed an O in position',num)
    draw_board(board)


if check_win(board) and player_win==True:
    print('Player wins!')
elif check_win(board):
    print('Computer wins!')
else:
    print("It's a tie!")