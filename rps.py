import random


def rps_game():
    user_wins = 0
    computer_wins = 0
    print("Welcome to Rock Paper Scissors Tug of War. Eliminate all computer's Os on the board to win. You both start with one icon.")
    board = ["X", "*", "*", "*", "*", "O"]
    print(board)
    user_icon_count = board.count("X")
    computer_icon_count = board.count("X")
    while board != ['X', 'X', 'X', 'X', 'X', 'X'] and board != ['O', 'O', 'O', 'O', 'O', 'O']:
        computer_choice = random.randrange(1, 4)
        user_choice = input("Rock, Paper, Scissors? ").lower()
        user_icon_count = board.count("X")
        computer_icon_count = board.count("O")

        if user_choice == 'rock' and computer_choice == 2:
            print("Computer chose scissors")
            print("User Wins!")
            user_wins += 1
            board[user_icon_count] = "X"
            

        elif user_choice == 'rock' and computer_choice == 3:
            print("Computer chose paper")
            print("Computer Wins :(")
            computer_wins += 1
            board[-(computer_icon_count + 1)] = "O"
            
            

        elif user_choice == "scissors" and computer_choice == 3:
            print("Computer chose paper")
            print("User Wins!")
            user_wins += 1
            board[user_icon_count] = "X"
            
        
        elif user_choice == "scissors" and computer_choice == 1:
            print("Computer chose rock")
            print("Computer Wins :(")
            computer_wins += 1
            board[-(computer_icon_count + 1)] = "O"
             

        elif user_choice == "paper" and computer_choice == 1:
            print("Computer chose rock")
            print("User Wins!")
            user_wins += 1
            board[user_icon_count] = "X"
            

        elif user_choice == "paper" and computer_choice == 2:
            print("Computer chose scissors")
            print("Computer Wins :(")
            computer_wins += 1
            board[-(computer_icon_count + 1)] = "O"
                 
        else:
            print("Tie!")
            
        score = f"User: {user_wins} | Computer: {computer_wins}"
        print(score)
        print(board)

    if board == ['X', 'X', 'X', 'X', 'X', 'X']:
        print("You won the rock paper scissors battle!")
    else: 
        print("Better luck next time!")

    print("That was fun! Let's do it again soon.")

rps_game()
play_again = input("In the mood for another battle?" )

while play_again == 'yes'[0]:
    rps_game()

print("Byeeee")
