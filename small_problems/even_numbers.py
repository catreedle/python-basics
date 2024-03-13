# Print all even numbers from 1 to 99,
# inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem
# by iterating over just the even numbers?

# for number in range(2, 100, 2):
#     print(number)
    
numbers = [number for number in range(1, 100) if not number % 2]
for number in numbers:
    print(number)
