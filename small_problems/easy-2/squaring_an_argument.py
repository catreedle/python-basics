# Squaring an Argument
# Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes
# the square of its argument (the square is the result of multiplying a number by itself).

def multiply(number1, number2):
    return number1 * number2

def square(number):
    return multiply(number, number)

# Examples
print(square(5) == 25)   # True
print(square(-8) == 64)  # True

# Further Exploration
# Suppose we want to generalize this function to a "power to the n" type function: cubed, to the 4th power, 
# to the 5th, etc. How would we go about doing so while still using the multiply function?
def power_to_n(base, n):
    result = 1
    for _ in range(n):
        result = multiply(result, base)
    
    return result

print(power_to_n(10, 10))