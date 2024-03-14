import random
import json
import os

with open('rps.json', 'r') as file:
    MESSAGE = json.load(file)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def messages(message, lang="en"):
    return MESSAGE[lang][message]

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
        return messages("tie")

    player_wins = {
        'rock': ('scissors', 'lizard'),
        'paper': ('rock', 'spock'),
        'scissors': ('paper', 'lizard'),
        'lizard': ('spock', 'paper'),
        'spock': ('scissors', 'rock')
    }

    if computer in player_wins[player]:
        return messages("player_win")
    return messages("computer_win")

def restart_game():
    answer = prompt_input(messages("restart")).lower()

    while not(answer in ('n', 'no') or answer in ('y', 'yes')):
        answer = prompt_input(messages("restart_invalid")).lower()

    if answer in ['y', 'yes']:
        clear_screen()
        winner = play_game()

        return winner
    return None

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
    result = ''
    if player_score == 3:
        result = 'Player'
    if computer_score == 3:
        result = 'Computer'
    return result

def reset_score(player_score, computer_score):
    player_score = 0
    computer_score = 0
    return player_score, computer_score

def play_game():
    choices = ', '.join(VALID_CHOICES.values())
    shorthand = ', '.join(VALID_CHOICES)
    choice = prompt_input(messages("input_choice").
                          format(choices=choices, shorthand=shorthand)).lower()

    choice = validate_input(choice, VALID_CHOICES)

    computer_choice = random.choice(list((VALID_CHOICES.values())))
    prompt(messages("display_choices").
           format(choice=choice, computer_choice=computer_choice))
    winner = get_winner(choice, computer_choice)
    return winner

def rock_paper_scissors():
    clear_screen()

    player_score = 0
    computer_score = 0

    choices = (', '.join(VALID_CHOICES.values()))
    prompt(messages("welcome").format(choices=choices))

    winner = play_game()
    prompt(winner)

    player_score, computer_score = count_score(winner,
                                               player_score, computer_score)

    prompt(messages("scores").
           format(player=player_score,computer=computer_score))

    while True:
        winner = restart_game()
        if winner:
            prompt(winner)
            player_score, computer_score = count_score(winner,
                                            player_score, computer_score)

            prompt(messages("scores").
                   format(player=player_score, computer=computer_score))

            winner_round = grand_winner(player_score, computer_score)

            if winner_round:
                prompt(messages("grand_winner").
                       format(winner_round=winner_round))

                player_score, computer_score = reset_score(
                    player_score, computer_score)
                prompt(messages("reset"))

        else:
            clear_screen()
            break

rock_paper_scissors()