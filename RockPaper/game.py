import random

exit = False
user_score = 0
comp_score = 0

while exit == False:
    options = ["rock","paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended")
        print(f"You total score is {user_score} and The computer score is {comp_score}")
        exit = True
    
    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock.")
            print("Computer input is rock.")
            print("It is a tie!")
        elif computer_input == "paper":
            print("Your input is rock.")
            print("Computer input is paper.")
            print("Computer Wins!")
            comp_score += 1            
        elif computer_input == "scissors":
            print("Your input is rock.")
            print("Computer input is scissors.")
            print("You Wins!")
            user_score += 1   
    elif user_input == "paper":
        if computer_input == "rock":
            print("Your input is paper.")
            print("Computer input is rock.")
            print("You win!")
            user_score += 1  
        elif computer_input == "paper":
            print("Your input is paper.")
            print("Computer input is paper.")
            print("It is a tie!")            
        elif computer_input == "scissors":
            print("Your input is paper.")
            print("Computer input is scissors.")
            print("Computer Wins!")
            comp_score += 1 
    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors.")
            print("Computer input is rock.")
            print("Computer wins!")
            comp_score += 1  
        elif computer_input == "paper":
            print("Your input is scissors.")
            print("Computer input is paper.")
            print("You win!") 
            user_score += 1            
        elif computer_input == "scissors":
            print("Your input is scissors.")
            print("Computer input is scissors.")
            print("It is a tie!")
    elif user_input != "paper" or user_input != "scissors" or user_input != "rock":
        print("Invalid User input!")
        