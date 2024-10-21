# a) Fazer um pedra, papel e tesoura melhor de 5 (que teria que usar o while).
# Melhor de 3 significa: Quem ganhar três primeiro vence.

import random

# Function to get user's choice
def get_user_choice():
    choice = input("Enter 'rock', 'paper', or 'scissor': ").lower().strip()
    if choice in ['rock', 'paper', 'scissor']:
        return choice
    else:
        print('Invalid choice, please choose "rock", "paper", or "scissor".')

# Function to get computer's random choice
def get_computer_choice():
    options = ['rock', 'paper', 'scissor']
    return random.choice(options)

# Function to determine the result
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Draw'
    # This is a ternary conditional expression
    return 'Win' if (user_choice == 'rock' and computer_choice == 'scissor') or \
                    (user_choice == 'paper' and computer_choice == 'rock') or \
                    (user_choice == 'scissor' and computer_choice == 'paper') \
                    else 'Defeat' 
    # elif user_choice == 'rock':
    #     if computer_choice == 'scissor':
    #         return "Win"
    #     else:
    #         return "Defeat"
    
    # elif user_choice == 'paper':
    #     if computer_choice == 'rock':
    #         return "Win"
    #     else:
    #         return "Defeat"
    
    # elif user_choice == 'scissor':
    #     if computer_choice == 'paper':
    #         return "Win"
    #     else:
    #         return "Defeat"

# Main function to run the game
def play_game():
    victories = 0
    rounds_played = 0
    max_rounds = 5

    while rounds_played < max_rounds:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}")

        if result == "Win":
            victories += 1
        
        rounds_played += 1
        print(f"\nRounds played: {rounds_played}/{max_rounds}\n")

    print(f"Total victories: {victories}")

# Start the game
play_game()

