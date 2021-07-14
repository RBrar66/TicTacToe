print("Easy Mode:            Press 1")
print("Hard Mode:            Press 2")
print("Impossible Mode:      Press 3")
print("Player vs Player      Press 4")

mode = input()
while not mode in ['1','2','3','4']:
    print("Please choose a number (1-4) to pick a mode!")
    mode = input()
if mode=='1':
    import tictactoe_AI_easy
elif mode=='2':
    import tictactoe_AI_hard
elif mode=='3':
    import tictactoe_AI_impossible
elif mode=='4':
    import tictactoe





