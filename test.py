import random
board = [["O", "", "_"], ["O", "", "_"], ["_", "_", "_"]]

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




computer_move()
print(board)

            

