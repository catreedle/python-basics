# Clean up the words
# Given a string that consists of some words and an assortment of non-alphabetic characters,
# write a function that returns that string with all of the non-alphabetic characters replaced by spaces.
# If one or more non-alphabetic characters occur in a row, you should only have one space 
# in the result (i.e., the result string should never have consecutive spaces).

def clean_up(string):
    
    clean_string = ''
    for char in string:
        if char.isalpha():
            clean_string += char
        elif not clean_string.endswith(' '):
            clean_string += ' '
                
    return clean_string

# Example
print(clean_up("---what's my +*& line?") == " what s my line ") # # True
