# The End Is Near But Not Here
# Write a function that returns the next to last word in the string argument.

# Words are any sequence of non-blank characters.

# You may assume that the input string will always contain at least two words.
# answer

def penultimate(string):
    words = string.split()
    return words[-2]

# further exploration
def validate_words(words):
    if words and len(words) >= 3:
        return True
    return False

def penultimate_middle(string):
    words = string.split()
    is_valid = validate_words(words)
    
    if is_valid:
        mid_index = (len(words) // 2)
        return words[mid_index]
    return ''
    
# Examples
# These examples should print True
print(penultimate_middle("last word"))
print(penultimate_middle("Launch School is great!") == "is")