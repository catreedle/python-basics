# How Old is Teddy?
# Build a program that randomly generates and prints Teddy's age. To get the age, you should generate 
# a random number between 20 and 100, inclusive.

# Further Exploration
# Modify this program to ask for a name, then print the age for that person. 
# For an extra challenge, use "Teddy" as the name if no name is entered.

import random
def display_age(name):
    age = random.randint(20, 100)
    print(f'{name} is {age} years old!')
    
name = input("Enter a name\n") or "Teddy"
display_age(name)

# Example Output
# Teddy is 69 years old!