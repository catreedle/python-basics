# Write a function that takes one integer argument and returns True
# when the number's absolute value is odd, False otherwise.

# START
# given an integer called "number"

# SET modulus = number % 2
# SET is_odd

# if modulus == 0
#   is_odd = False
# else
#   is_odd = True
# PRINT is_odd
# END

def check_if_odd(value):
    '''
    A function that takes one integer argument and returns True
    when the number's absolute value is odd, False otherwise.
    '''
    modulus = abs(int(value)) % 2
    if modulus == 0:
        return False
    return True

def is_valid(value):
    '''
    A function to check if value is a valid integer number.
    '''
    try:
        int(value)
    except ValueError:
        return False
    return True

while True:
    print('>> Please insert an integer number.')
    number = input()
    if is_valid(number):
        break


IS_ODD = check_if_odd(number)
print(f'>> Is your number {number} odd?')
print(IS_ODD)