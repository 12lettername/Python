board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def game_board():
    print(board[1], board[2], board[3], sep="|")
    print("-----")
    print(board[4], board[5], board[6], sep="|")
    print("-----")
    print(board[7], board[8], board[9], sep="|")


def check():
    global game_on
    if board[1] == board[2] == board[3] == marker1 or board[4] == board[5] == board[6] == marker1 or board[7] == board[
        8] == board[9] == marker1 or board[1] == board[4] == board[7] == marker1 or board[2] == board[5] == board[
        8] == marker1 or board[3] == board[6] == board[9] == marker1 or board[1] == board[5] == board[9] == marker1 or \
            board[3] == board[5] == board[7] == marker1:
        print(f"{player1} won the game")
        game_on = False
        game_board()
    elif board[1] == board[2] == board[3] == marker2 or board[4] == board[5] == board[6] == marker2 or board[7] == \
            board[8] == board[9] == marker2 or board[1] == board[4] == board[7] == marker2 or board[2] == board[5] == \
            board[8] == marker2 or board[3] == board[6] == board[9] == marker2 or board[1] == board[5] == board[
        9] == marker2 or board[3] == board[5] == board[7] == marker2:
        print(f"{player2} won the game")
        game_on = False
        game_board()
    elif board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] \
            != " " and board[7] != " " and board[8] != " " and board[9] != " ":
        print("The game is a tie")
        game_on = False
        game_board()
    else:
        game_on = True


def choose_marker():
    marker1 = "wrong"
    while marker1 not in ["X", "O"]:
        marker1 = input(f"{player1} choose your marker(X/O): ")
        if marker1 not in ["X", "O"]:
            print("Sorry Invalid choice, please try again")
    return marker1



print("Here is the TIC - TAC - TOE board!")
game_board()
player1 = input("Enter the name of player1: ")
player2 = input("Enter the name of player2: ")
game_on = True
marker2 = ""
marker1 = choose_marker()
if marker1 == "X":
    marker2 = "O"
else:
    marker2 = "X"
turn = 0
checker = []
while game_on:
    clear_output()
    game_board()
    choice = 0
    while choice not in range(1, 10) or choice in checker:
        choice = int(input("Enter your choice(1-9): "))
        if choice not in range(1, 10) or choice in checker:
            print("Incorrect choice, TRY AGAIN")
    checker.append(choice)
    if turn % 2 == 0:
        board[choice] = marker1
    elif turn % 2 != 0:
        board[choice] = marker2
    check()
    turn += 1
