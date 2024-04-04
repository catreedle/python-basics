# Sum or Product of Consecutive Integers
# Write a program that asks the user to enter an integer greater than 0, 
# then asks whether the user wants to determine the sum or the product of all numbers 
# between 1 and the entered integer, inclusive.

def get_input(prompt):
    value = input(prompt)
    return value

while True:
    try:
        integer = int(get_input('Please enter an integer greater than 0: '))
        if integer > 0:
            break
        else:
            print('Please enter a positive number.')
    except ValueError:
        print('Please enter a valid integer number.')
    
while True:
    calculation_type = get_input('Enter "s" to compute the sum, or "p" to compute the product. ')
    if calculation_type.lower() in ['s', 'p']:
        break
    else:
        print('Your input is invalid.')

def calculate_sum(value):
    sum_value = 0
    for number in range(1, value+1):
        sum_value += number
        
    return sum_value

def calculate_product(value):
    product_value = 1
    for number in range(1, value+1):
        product_value *= number
        
    return product_value

def display_sum_or_product(integer, calculation_type):
    print()
    
    if calculation_type == 's':
        print(f'The sum of the integers between 1 and {integer} is {calculate_sum(integer)}.')
    else:
        print(f'The product of the integers between 1 and {integer} is {calculate_product(integer)}.')

display_sum_or_product(integer, calculation_type)