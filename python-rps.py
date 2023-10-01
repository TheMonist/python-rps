import random

while True:
    print("Choose: Rock, Paper, or Scissors")

    possible_choice = ["Rock", "Paper", "Scissors"]

    player_option = input("Make a choice: ")

    computer_option = random.choice(possible_choice)

    print(f"You chose {player_option} and the computer chose {computer_option}")

    if (player_option == computer_option):
        print("It's a tie")
    elif (player_option.upper() == "rock" and computer_option == "paper"):
        print("Computer Wins!")
    elif (player_option.upper() == "paper" and computer_option == "rock"):
        print("Player Wins!")
    elif(player_option.upper() == "paper" and computer_option == "scissors"):
        print("Computer Wins!")
    elif (player_option.upper() == "scissors" and computer_option == "paper"):
        print("Player Wins!")
    elif (player_option.upper() == "scissors" and computer_option == "rock"):
        print("Computer Wins")
    elif(player_option.upper() == "rock" and computer_option == "scissors"):
        print("Player Wins!")
    
    play_again = input("Play Again? (Y / N): ")
    if (play_again.upper() == "N"):
        break
