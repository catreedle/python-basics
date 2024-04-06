# Bannerizer
# Write a function that takes a short line of text and prints it within a box.

def print_in_box(string):
    str_length = len(string)
    dashes = '-' * str_length
    spaces = ' ' * str_length
    print(f'+-{dashes}-+')
    print(f'| {spaces} |')
    print(f'| {string} |')
    print(f'| {spaces} |')
    print(f'+-{dashes}-+')
# Example 1
print_in_box('To boldly go where no one has gone before.')
# Output for Example 1Copy Code
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+
# Example 2
print_in_box('')
# Output for Example 2Copy Code
# +--+
# |  |
# |  |
# |  |
# +--+
# You may assume the output will always fit in your terminal window.

