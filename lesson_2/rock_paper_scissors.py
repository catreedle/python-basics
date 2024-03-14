import random
import json

with open('rps.json', 'r') as file:
    MESSAGE = json.load(file)

def clear_screen():
    print("\033[H\033[J")  # ANSI escape code to clear the screen

def messages(message, lang="en"):
    return MESSAGE[lang][message]

VALID_CHOICES = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'l': 'lizard',
    'sp': 'spock'
}

VALID_CHOICES_VALUES = list(VALID_CHOICES.values())
WINNING_SCORE = 3

def prompt(message):
    # display message with formatting
    print(f'>>>{message}')

def get_user_input(prompt_message):
    # return input from user while displaying formatted input prompt
    return input(f'>>>{prompt_message}').lower()

def get_winner(player, computer):
    # return the winner based on game rules
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
    # ask if user want to continue playing the game
    answer = get_user_input(messages("restart"))
    while answer not in ('n', 'no', 'y', 'yes'):
        answer = get_user_input(messages("restart_invalid"))

    clear_screen()
    return answer in ['y', 'yes']

def validate_input(value):
    # validate that user input is in VALID_CHOICES keys or VALID_CHOICES values
    while value not in VALID_CHOICES_VALUES:
        if value in VALID_CHOICES:
            value = VALID_CHOICES.get(value)
        else:
            value = get_user_input("That's not a valid choice\n")

    return value

def update_score(winner, player_score, computer_score):
    # update player or computer score based on the winner
    match winner:
        case 'You win!':
            player_score += 1
        case 'Computer wins!':
            computer_score += 1
    return player_score, computer_score

def display_scores(player_score, computer_score):
    # display current score of player and computer
    prompt(messages("scores").
           format(player=player_score,computer=computer_score))

def grand_winner(player_score, computer_score):
    # return winner when one of the two opponent reaches WINNING_SCORE first
    result = ''
    if player_score == WINNING_SCORE:
        result = 'player'
    if computer_score == WINNING_SCORE:
        result = 'computer'
    return result

def reset_score(player_score, computer_score):
    player_score = 0
    computer_score = 0
    return player_score, computer_score

def initialize_game():
    clear_screen()
    player_score = 0
    computer_score = 0
    return player_score, computer_score

def get_player_choice():
    # get player choice from user input and validate the input
    choices = ', '.join(VALID_CHOICES_VALUES)
    shorthand = ', '.join(VALID_CHOICES)

    choice = get_user_input(messages("input_choice").
                          format(choices=choices, shorthand=shorthand))
    choice = validate_input(choice)

    return choice

def get_computer_choice():
    # randomly return a choice from VALID_CHOICES_VALUES
    computer_choice = random.choice(VALID_CHOICES_VALUES)
    return computer_choice

def play_round():
    # get player and computer choices
    choice = get_player_choice()
    computer_choice = get_computer_choice()

    # display player and computer choices
    prompt(messages("display_choices").
           format(choice=choice, computer_choice=computer_choice))
    # get winner based on those choices
    winner = get_winner(choice, computer_choice)
    return winner

def play_game():
    player_score, computer_score = initialize_game()
    choices = ', '.join(VALID_CHOICES_VALUES)

    prompt(messages("welcome").format(choices=choices))

    while True:
        # continue playing the game after user input to stop
        winner = play_round()
        prompt(winner)
        player_score, computer_score = update_score(winner,
                                    player_score, computer_score)
        display_scores(player_score, computer_score)

        winner_match = grand_winner(player_score, computer_score)
        if winner_match:
            if winner_match == 'player':
                prompt(messages("grand_winner_player"))
            else:
                prompt(messages("grand_winner_computer"))
            player_score, computer_score = reset_score(
                player_score, computer_score)

            prompt(messages("reset"))

        if not restart_game():
            clear_screen()
            break

play_game()