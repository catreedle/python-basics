# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate.
# The program must compute the tip, then print both the tip and the total amount of the bill. 
# You can ignore input validation and assume that the user will enter valid numbers.

def prompt_input(prompt):
    return float(input(prompt))

bill_amount = prompt_input('What is the bill? ')
tip_percentage = prompt_input('What is the tip percentage? ')

def calculate_tip(bill_amount, tip_percentage):
    tip = bill_amount * (tip_percentage / 100)
    return tip

def calculate_total(bill_amount, tip):
    total = bill_amount + tip
    return total

def display_tip_and_total(bill_amount, tip_percentage):
    tip = calculate_tip(bill_amount, tip_percentage)
    total = calculate_total(bill_amount, tip)
    
    print(f'The tip is ${tip:.2f}')
    print(f'The total is ${total:.2f}')

display_tip_and_total(bill_amount, tip_percentage)
