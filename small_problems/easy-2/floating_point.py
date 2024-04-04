# Floating Point Arithmetic
# Write a program that prompts the user for two positive numbers (floating-point), then prints the results
# of the following operations on those two numbers: addition, subtraction, product, quotient, 
# floor quotient, remainder, and power. Do not worry about validating the input.

# Examples
# ==> Enter the first number:
# 3.141529
# ==> Enter the second number:
# 2.718282
# ==> 3.141529 + 2.718282 = 5.859811
# ==> 3.141529 - 2.718282 = 0.42324699999999993
# ==> 3.141529 * 2.718282 = 8.539561733178
# ==> 3.141529 / 2.718282 = 1.1557038600115808
# ==> 3.141529 // 2.718282 = 1.0
# ==> 3.141529 % 2.718282 = 0.42324699999999993
# ==> 3.141529 ** 2.718282 = 22.45792517468373

def prompt(string):
    return f'==> {string}'
    
first_number = float(input(prompt("Enter the first number:\n")))
second_number = float(input(prompt("Enter the second number:\n")))

def display_operations_result(number1, number2):
    print(prompt(f'{number1} + {number2} = {number1 + number2}'))
    print(prompt(f'{number1} - {number2} = {number1 - number2}'))
    print(prompt(f'{number1} * {number2} = {number1 * number2}'))
    print(prompt(f'{number1} / {number2} = {number1 / number2}'))
    print(prompt(f'{number1} // {number2} = {number1 // number2}'))
    print(prompt(f'{number1} % {number2} = {number1 % number2}'))
    print(prompt(f'{number1} ** {number2} = {number1 ** number2}'))
    
display_operations_result(first_number, second_number)