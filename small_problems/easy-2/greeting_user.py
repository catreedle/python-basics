# Greeting a user
# Write a program that asks for user's name, then greets the user. If the user appends a ! to their name,
# the computer will yell the greeting (print it using all uppercase).

# Example 1
# What is your name? Sue
# Hello Sue.
# Example
# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?

def greeting_a_user():
    name = input("What is your name? ")
    if name and name.endswith('!'):
        print(f"HELLO {name.upper()} WHY ARE WE YELLING?")
    else:
        print(f"Hello {name}.")

greeting_a_user()