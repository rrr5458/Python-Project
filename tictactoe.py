import random

board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

def check_done(): 
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2] == "O" \
        or board[0][i] == board[1][i] == board[2][i] == "O":
            print("You won!")
            return True
        
        if board[i][0] == board[i][1] == board[i][2] == "X" \
        or board[0][i] == board[1][i] == board[2][i] == "X":
            print("You lost")
            return True
         
    if board[0][0] == board[1][1] == board[2][2] == "O" \
    or board[0][2] == board[1][1] == board[2][0] == "O":
            print("You won!")
            return True

    if board[0][0] == board[1][1] == board[2][2] == "X" \
    or board[0][2] == board[1][1] == board[2][0] == "X":
            print("You lost!")
            return True
 
    if "_" not in board[0] and "_" not in board[1] and "_" not in board[2]:
        print("Cat game")
        return True
    
    return False

def computer_move():
    for i in range(0,3):
        if board[i][0] == board[i][1] == "O":
            if board[i][2] == "_":
                board[i][2] = "X"
                return True
        elif board[0][i] == board[1][i] == "O":
            if board[2][i] == "_":
                board[2][i] = "X"
                return True 
        elif board[i][0] == board[i][2] == "0":
            if board[i][1] == "_":
                board[i][1] =="X"
                return True
        elif board[0][i] == board[2][i] == "O":
            if board[1][i] == "_":
                board[1][i] = "X"
                return True
        elif board[i][1] == board[i][2] == "O":
            if board[i][0] == "_":
                board[i][0] = "X"
                return True
        elif board[1][i] == board[2][i] == "O":
            if board[0][i] == "_":
                board[0][i] = "X"
                return True

    if board[0][0] == board[1][1] == "O":
        board[2][2] = "X"
        return True
    elif board [2][2] == board[1][1] == "O":
        board[0][0] = "X"
        return True
    elif board [0][2] == board[1][1] == "O":
        board[2][0] = "X"
        return True
    elif board[1][1] == board[2][0] == "O":
        board[0][2] = "X"
        return True 
def board_printer():
    for i in board:
        print(i)

def turn():
    done = False
    while done == False:
        user_choice_row = int(input("Row?"))
        user_choice_column = int(input("Column?"))
        while board[user_choice_row - 1][user_choice_column - 1] == "X" or board[user_choice_row - 1][user_choice_column - 1] == "O":
            print("That space has already been marked")
            user_choice_row = int(input("Row?"))
            user_choice_column = int(input("Column?"))

        board[user_choice_row - 1][user_choice_column - 1] = "O"
        done = check_done()

        if computer_move() != True:
            computer_choice = (random.randrange(0, 3), random.randrange(0, 3)) #how to build AI
            while board[computer_choice[0]][computer_choice[1]] == "X" or board[computer_choice[0]][computer_choice[1]] == "O":
                computer_choice = (random.randrange(0, 3), random.randrange(0, 3))
            board[computer_choice[0]][computer_choice[1]] = "X"
        board_printer()

turn()
play_again = input("Do you want to play again?")[0]
while play_again == "y":
    board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    turn()

print("Let's play again soon.")