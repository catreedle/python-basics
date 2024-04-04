# When Will I Retire?
# Build a program that displays when the user will retire and how many years she has to work till retirement.

# Example
# What is your age? 30
# At what age would you like to retire? 70

# It's 2024. You will retire in 2064.
# You have only 40 years of work to go!
from datetime import date
age = int(input("What is your age? "))
age_retired = int(input("At what age would you like to retire? "))
working_years = age_retired - age

year_today = date.today().year
year_retired = year_today + (working_years)

print(f"It's {year_today}. You will retire in {year_retired}.")
print(f"You have only {working_years} years of work to go!")