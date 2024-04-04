import math

#  1. Let's do some "ASCII Art": a stone-age form of nerd artwork from back in the days before computers
# had video screens.

# For this practice problem, write a program that outputs The Flintstones Rock! 10 times, 
# with each line indented 1 space to the right of the line above it. The output should start out like this:

string = 'The Flintstones Rock!'
for line in range(1, 11):
    print(" " * line, string)
    
# 2 Alan wrote the following function, which was intended to return all of the factors of number:
def factors(number):
    divisor = number
    result = []
    while divisor != 0:
    # should be
    # while divisor > 0
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result
# Alyssa noticed that this code would fail when the input is a negative number, 
# and asked Alan to change the loop. How can he make this work? Note that we're not looking to 
# find the factors for negative numbers, but we want to handle it gracefully instead of going 
# into an infinite loop.

# Bonus: Question: What is the purpose of number % divisor == 0 in that code?
# The purpose is to check whether the result of the division has no remainder, if the result has
# no remainder, it means it is is an integer, thus divisor is a factor of number.
# of that number.

# 3. Alyssa was asked to write an implementation of a rolling buffer.
# You can add and remove elements from a rolling buffer. However, once the buffer becomes full,
# any new elements will displace the oldest elements in the buffer.

# She wrote two implementations of the code for adding elements to the buffer:
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# Is there a difference between these implementations, other than the way she is adding an element 
# to the buffer?
# The difference is the first function mutate buffer directly, while the second function creates a new
# variable buffer and assign it the value of the original buffer add new_element.

# 5. What do you think the following code will output?
nan_value = float("nan")

print(nan_value == float("nan"))
# answer: this will output false because nan values have peculiar property that they are not equal 
# to themselves according to IEEE 754 standard.
# Python doesn't let you use == to determine whether a value is nan.
# Bonus: How can you reliably test if a value is nan?
# using the math module built in function isnan
print(math.isnan(nan_value))
print(nan_value, float('nan'))

# 8. Function and method calls can take expressions as arguments. Suppose we define a function named
# rps as follows, which follows the classic rules of the rock-paper-scissors game, but with 
# a slight twist: in the event of a tie, it just returns the choice made by both players.

def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"
# What does the following code output?
print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))
#               "paper"             "rock"
#                            "paper"                           "rock"
#       paper

# 9. Consider these two simple functions:
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"
# What will the following function invocation return?

# bar(foo()) ==> bar("yes")
# this evaluates to ("yes" == "no" and "yes") or "no"
# the left side of or expression evaluates to False, therefore we return the right side of the expression ("no")

