# Strings Strings
# Write a function that takes one argument, a positive integer, and returns a string of alternating '1's 
# and '0's, always starting with a '1'. The length of the string should match the given integer.

def stringy(number):
    one_zeroes = '1'
    
    while len(one_zeroes) < number:
        if one_zeroes[-1] == '1':
            one_zeroes += '0'
        else:
            one_zeroes += '1'
    
    return one_zeroes

# Examples
print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")    