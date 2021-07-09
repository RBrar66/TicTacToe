def draw_board(board):
    print(board[0][0],'|',board[0][1],'|',board[0][2])
    print('---------')
    print(board[1][0],'|',board[1][1],'|',board[1][2])
    print('---------')
    print(board[2][0],'|',board[2][1],'|',board[2][2])
def check_win(board):
    for x in range(3):
        if(board[x][0]==board[x][1]==board[x][2] or board[0][x]==board[1][x]==board[2][x]):
            return True
    return(board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0])
def check_tie(board):
    for x in range(49, 58):
        if(chr(x) in board[0] or chr(x) in board[1] or chr(x) in board[2]):
            return False
    return True

board = [['1','2','3'],['4','5','6'],['7','8','9']]
finish = False
draw_board(board)
filled = []
player = 1
while(not finish):
    print('Player ', player, ': Choose a number:  ')
    num = input()
    while(num in filled or not (len(num)==1 and num != "0") or ord(num)-48>9 or ord(num)-48<1):
        print('Player ', player, ': You must choose a valid number (1-9) that is not already taken:  ')
        num = input()
    num2 = ord(num) - 48
    filled.append(num)
    if(player == 1):
        board[(num2-1)//3][(num2-1)%3] = 'X'
    if (player == 2):
        board[(num2-1)//3][(num2-1)%3] = 'O'
    draw_board(board)
    if(player==1):
        player = 2
    else:
        player = 1
    finish = check_win(board) or check_tie(board)
if(check_win(board) and player==1):
    print('Player 2 wins!')
elif(check_win(board)):
    print('Player 1 wins!')
else:
    print("It's a tie!")