import json

# Open the JSON file for reading
with open('file.json', 'r') as file:
    MESSAGE = json.load(file)

# Now 'MESSAGE' contains the contents of the JSON file
# as a Python dictionary or list

def prompt(message):
    print(f'==> {message}')

def messages(message, lang="id"):
    return MESSAGE[lang][message]

prompt(messages("welcome"))

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

while True: # looping through calculator process
# Ask the user for the first number.
    prompt(messages("first_number"))
    number1 = input()

    while invalid_number(number1):
        prompt(messages("invalid_number"))
        number1 = input()

    # Ask the user for the second number.
    prompt(messages("second_number"))
    number2 = input()

    while invalid_number(number2):
        prompt(messages("invalid_number"))
        number2 = input()

    # Ask the user for an operation to perform.
    prompt(messages("operation"))
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(messages("invalid_operation"))
        operation = input()

    # Perform the operation on the two numbers.
    match operation:
        case '1': # '1' represents addition
            output = float(number1) + float(number2)
        case '2': # '2' represents subtraction
            output = float(number1) - float(number2)
        case '3': # '3' represents multiplication
            output = float(number1) * float(number2)
        case '4': # '4' represents division
            if float(number2) == 0:
                prompt(messages("division_by_zero"))
                exit(1)
            output = float(number1) / float(number2)

    output = round(output, 2) # Round the result to two decimals

    prompt(messages("result").format(output=output))
    # Print the result to the terminal.
    prompt(messages("restart"))
    # prompt input to restart calculator
    restart = input()
    if restart != 'yes':
        break