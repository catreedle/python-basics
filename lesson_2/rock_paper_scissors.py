import random

VALID_CHOICES = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'l': 'lizard',
    'sp': 'spock'
}

def prompt(message):
    print(f'>>>{message}')

def prompt_input(message):
    return input(f'>>>{message}')

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"

    player_wins = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }

    if computer in player_wins[player]:
        return 'You win!'
    return 'Computer wins!'

def restart_game():
    answer = prompt_input("Do you want to play again? (y/n)?\n").lower()
    while not(answer.startswith('n') or answer.startswith('y')):
        answer = prompt_input('Please enter "y" or "n".\n').lower()
    if answer.startswith('y'):
        winner = play_game()
        return winner

def validate_input(value, values_dict):
    while value not in values_dict.values():
        if value in values_dict.keys():
            value = values_dict[value]
        else:
            value = prompt_input("That's not a valid choice\n")
    return value

def count_score(winner, player_score, computer_score):
    match winner:
        case 'You win!':
            player_score += 1
        case 'Computer wins!':
            computer_score += 1
    return player_score, computer_score

def grand_winner(player_score, computer_score):
    if player_score == 3:
        return 'Player'
    if computer_score == 3:
        return 'Computer'

def reset_score(player_score, computer_score):
    player_score = 0
    computer_score = 0
    return player_score, computer_score

def play_game():
    choice = prompt_input(f'''Choose one: {', '.join(VALID_CHOICES.values())}
    or the initials: {', '.join(VALID_CHOICES.keys())}\n''').lower()

    choice = validate_input(choice, VALID_CHOICES)

    computer_choice = random.choice(list((VALID_CHOICES.values())))
    prompt(f'You chose {choice}, computer chose {computer_choice}')
    winner = get_winner(choice, computer_choice)
    return winner

# play_game()

def rock_paper_scissors():
    player_score = 0
    computer_score = 0
    winner = play_game()
    prompt(winner)
    player_score, computer_score = count_score(winner, player_score, computer_score)
    prompt(f'Player: {player_score}, Computer: {computer_score}')
    while True:
        winner = restart_game()
        prompt(winner)
        player_score, computer_score = count_score(winner, player_score, computer_score)
        prompt(f'Player: {player_score}, Computer: {computer_score}')
        winner_round = grand_winner(player_score, computer_score)
        if winner_round:
            prompt(f'{winner_round} is Grand Winner!')
            player_score, computer_score = reset_score(player_score, computer_score)
        if not winner:
            break
    
rock_paper_scissors()