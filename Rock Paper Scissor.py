import random

user_wins = 0
computer_wins = 0

play_game = input("Welcome to Rock, Paper, Scissors! Do you wish to continue? (Y/N): ")
options = ["Rock", "Scissors", "Paper"]

if play_game.upper() == "Y":
    while True:
        random_number = random.randint(0, 2)
        computer_choice = options[random_number]
        
        print("\nPlease remember to only use the specified letters!")
        user_choice = input("Choose R for rock, S for scissors, P for paper and Q to quit the game: ")
        user_choice = user_choice.upper()  # Convert to uppercase for easier comparison
        
        # Handle quit option
        if user_choice == "Q":
            print("Thanks for playing! Final Score:")
            print(f"Computer - {computer_wins} | User - {user_wins}")
            print("Goodbye!!!")
            break
        
        # Validate input
        if user_choice not in ["R", "S", "P"]:
            print("Invalid input! Please use R, S, P, or Q only. 😑")
            continue
        
        # Convert user choice to full word for display
        user_display = {"R": "Rock", "S": "Scissors", "P": "Paper"}[user_choice]
        
        # Check for draw
        if (user_choice == "R" and computer_choice == "Rock") or \
           (user_choice == "S" and computer_choice == "Scissors") or \
           (user_choice == "P" and computer_choice == "Paper"):
            print(f"\nThe computer picked {computer_choice} and you picked {user_display}.")
            print("It's a draw!")
        
        # Check for user wins
        elif (user_choice == "R" and computer_choice == "Scissors") or \
             (user_choice == "S" and computer_choice == "Paper") or \
             (user_choice == "P" and computer_choice == "Rock"):
            user_wins += 1
            print(f"\nThe computer picked {computer_choice} and you picked {user_display}.")
            print("You win!")
        
        # Computer wins (remaining cases)
        else:
            computer_wins += 1
            print(f"\nThe computer picked {computer_choice} and you picked {user_display}.")
            print("You lose!")
        
        # Display current score
        print(f"Score: Computer - {computer_wins} | User - {user_wins}")

elif play_game.upper() == "N":
    print("Goodbye!!!")
else:
    print("Please enter Y or N next time!")