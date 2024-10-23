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
        return get_user_choice()

# Function to get computer's random choice
def get_computer_choice():
    options = ('rock', 'paper', 'scissor')
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
    
# Main function to run the game
def play_game():
    user_victories = 0
    computer_victories = 0
    rounds_played = 0
    max_victories = 3

    # while rounds_played < max_rounds:
    while user_victories < max_victories and computer_victories < max_victories:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}")

        if result == 'Win':
            user_victories += 1

        elif result == 'Defeat':
            computer_victories += 1

        print(f"\nUser victories: {user_victories}")
        print(f"Computer victories: {computer_victories}")

        rounds_played += 1
        print(f"\nRounds played: {rounds_played}\n")
    
    if user_victories == max_victories:
        print("Congratulations, you won the game!😊😊\n")
    else:
        print("Sorry, the computer won the game!😥😥\n")

# Start the game
play_game()


# b) Conseguem resolver meu exercício de cálculo 4?? Vocês tem que avaliar,
# com loops que a gente já aprendeu, se essa série, somando “todos” os
# termos vai ou não vai convergir para um valor.


import math

def series_term(n):
    """Calculate the nth term of the series 1 / (n * ln^2(n))."""
    if n > 1:
        return 1 / (n * (math.log(n)) ** 2)
    return 0

def check_convergence(threshold=1e-6, max_iterations=1000000):
    """Sum the series and stop when the difference between terms is less than the threshold."""
    n = 2  # Start from n=2
    sum_series = 0
    prev_sum = 0  # To track the previous sum value
    iterations = 0

    while iterations < max_iterations:
        term = series_term(n)
        sum_series += term
        
        # Calculate the difference between the current and previous sum
        difference = abs(sum_series - prev_sum)
        
        # Print the current value of n, the term, and the sum
        print(f"n={n}, term={term}, sum={sum_series}, difference={difference}")
        
        # Check if the change in sum is less than the threshold
        if difference < threshold:
            print("\nThe series seems to converge.")
            break
        
        # Update values for the next iteration
        prev_sum = sum_series
        n += 1
        iterations += 1
    
    if iterations == max_iterations:
        print(f"Reached the maximum number of iterations ({max_iterations}).")
    
    return sum_series

# Run the convergence check
final_sum = check_convergence()
print(f"\nFinal sum of the series: {final_sum}\n")
