# Exclusive Or
# The or operator returns a truthy value if either or both of its operands are truthy, a falsy value if
# both operands are falsy. The and operator returns a truthy value if both of its operands are truthy,
# and a falsy value if either operand is falsy. This works great until you need only one of two conditions
# to be truthy, the so-called exclusive or, also known as xor (pronounced "ECKS-or").

# In this exercise, you will write an xor function that takes two arguments, and returns True if exactly
# one of its arguments is truthy, False otherwise.

# answer
def xor(a, b):
    if (a and not b) or (b and not a):
        return True
    return False

# Copy Code
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)