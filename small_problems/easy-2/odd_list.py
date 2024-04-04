# Odd Lists
# Write a function that returns a list that contains every other element of a list that is passed in as 
# an argument. The values in the returned list should be those values that are in the 1st, 3rd, 5th,
# and so on elements of the argument list.

# answer
def oddities(list):
    # every_other_list = []
    # for index in range(len(list)):
    #     if index % 2 == 0:
    #         every_other_list.append(list[index])
    
    # return every_other_list

    # bonus question
    return list[::2]

def evenness(list):
    return [list[idx] for idx in range(len(list)) if idx % 2]
        
# Examples
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(evenness([1, 2, 3, 4, 5]))
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True
# Bonus question: Try to solve the problem using list slicing.

