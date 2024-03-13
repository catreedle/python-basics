import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'>>>{message}')

def prompt_input(message):
    return input(f'>>>{message}')

def display_winner(player, computer):
    if ((player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')):
        return 'You win!'
    elif ((player == 'rock' and computer == 'paper') or
        (player == 'paper' and computer == 'scissors') or
        (player == 'scissors' and computer == 'rock')):
        return 'Computer wins!'
    else:
        return 'It\'s a tie!'

def restart_game():
    answer = prompt_input("Do you want to play again? (y/n)?\n").lower()
    while not(answer.startswith('n') or answer.startswith('y')):
        answer = prompt_input('Please enter "y" or "n".\n').lower()
    if answer.startswith('y'):
        play_game()

def play_game():
    choice = prompt_input(f"Choose one: {', '.join(VALID_CHOICES)}\n")

    while choice not in VALID_CHOICES:
        choice = prompt_input("That's not a valid choice\n")

    computer_choice = random.choice(VALID_CHOICES)
    prompt(f'You chose {choice}, computer chose {computer_choice}')
    prompt(display_winner(choice, computer_choice))
    restart_game()

play_game()

