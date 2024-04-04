# 1. Write two different ways to remove all of the elements from the following list:
numbers = [1, 2, 3, 4]
# answer
# 1
numbers.clear()
# 2
for _ in range(len(numbers)):
    numbers.pop()