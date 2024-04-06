# What Century is That?
# Write a function that takes a year as input and returns the century. The return value should be 
# a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' 
# as appropriate for that number.

# New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.

import math

def century(year):
    str_century = str(math.ceil (year / 100))
    
    if (str_century.endswith('1') and not str_century.endswith('11')):
        str_century += 'st'
    elif (str_century.endswith('02') or str_century == '2'):
        str_century += 'nd'
    elif (str_century.endswith('03') or str_century == '3'):
        str_century += 'rd'
    else:
        str_century += 'th'
        
    return str_century

# Examples
print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True