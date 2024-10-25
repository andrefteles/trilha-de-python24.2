# a) Fazer um jogo da forca dentro do python

import os
from rich.console import Console
from rich.panel import Panel

# Function to print welcome message
def print_welcome_message(secret_word):
    console = Console()
    terminal_width = os.get_terminal_size().columns
    
    text = f'''Welcome to the hangman.
Try to find a correct letter or your character will die slowly.
The secret word has {len(secret_word)} letters.
Let's start.\n'''

    # Center the panel content
    panel = Panel(
        text.center(terminal_width - 10),       # Adjust width to center content inside the panel
        title='Hangman Game',   # Title for the panel
        border_style='cyan',    # Change the border color
        padding=(1, 1)          # Adjust the padding inside the panel
    )
    
    # Print the panel
    console.print(panel)

# Function to handle the user input
def get_user_input():
    while True:
        user_letter = input('Enter a letter: ').strip().lower()
        if len(user_letter) != 1 or not user_letter.isalpha():
            print('\nEnter only one vallid letter.\n')
            # return False
        else:
            return user_letter

# Function to update the displayed word
def update_completed_word(secret_word, correct_letter):
    completed_word = ''    
    for secret_letter in secret_word:
        if secret_letter in correct_letter:
                completed_word += secret_letter
        else:
            completed_word += '*'
    return completed_word  

def track_mistakes(mistake, max_mistakes):
    remaining_attempts = 1 + max_mistakes - mistake

    if remaining_attempts == 0:
        print('\nGame over! You ran out of attempts.')
        # print(f'The secret word was {secret_word}.\n')
        return False
    else:
        print(f'\nWrong guess! You have {remaining_attempts} attempts left.\n')
        return True

# Function to check for victory
def check_victory(secret_word, completed_word):
    if completed_word == secret_word:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
        print('You win!! Congratulations!')
        print(f'The secret word was {secret_word}\n')
        return True
    return False

# Main function to run the game
def hangman(): 
    secret_word = 'vasco'
    correct_letter = ''
    mistake = 0
    max_mistakes = 5    # Maximum allowed mistakes
    
    print_welcome_message(secret_word)

    while True:
        user_letter = get_user_input()
        
        if user_letter in secret_word:
            correct_letter += user_letter
        else:
            mistake += 1
            
            if not track_mistakes(mistake, max_mistakes):
                    print(f'The secret word was {secret_word}.\n')
                    break

            continue  # Restart the loop

        completed_word = update_completed_word(secret_word, correct_letter)
        
        print(f'\ncompleted word: {completed_word}\n')

        if check_victory(secret_word, completed_word):
            break

# Start the game
hangman()