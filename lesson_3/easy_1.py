# 1. Will the code below raise an error?
numbers = [1, 2, 3]
# numbers[6] = 5
# answer
# Code will raise IndexError because we're trying to access the element of numbers list that doesn't exist.
# We're trying to reassign element at index 6 when the last index of numbers is 2,
# thus index 6 being out of range.

# 2. How can you determine whether a given string ends with an exclamation mark (!)?
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False
# We can use string method endswith that takes one parameter and returns boolean based on 
# whether the string ends with that parameter
# answer
print(str1.endswith('?'))
print(str2.endswith('?'))
# We can also use the slicing method, taking the last character of the string and 
# comparing it with a specific string.
print(str1[-1] == '?')
print(str2[-1] == '?')

# 3. Starting with the string below, Show two different ways to put the expected 
# "Four score and " in front of it.
famous_words = "seven years ago..."
# answer
famous_words = "Four score and " + famous_words
famous_words = f"Four score and {famous_words}" 

# 4. Using the following string, create a new string that contains all lowercase letters 
# except for the first character, which should be capitalized.
munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
# answer
munsters_description.capitalize()

# 5. Starting with the string:
munsters_description = "The Munsters are creepy and spooky."
# Return a new string that swaps the case of all of the letters:
# "tHE mUNSTERS ARE CREEPY AND SPOOKY."
# answer
munsters_description.swapcase()

# 6. Determine whether the name Dino appears in the strings below -- check each string separately:
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

# answer
print('Dino' in str1)
print('Dino' in str2)

# 7. How can we add the family pet, "Dino", to the following list?
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# answer
flintstones.append('Dino')

# 8. In the previous problem, our first answer added 'Dino' to the list like this:
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")
# How can we add multiple items to our list (e.g., 'Dino' and 'Hoppy')? 
# Replace the call to append with another method invocation.
flintstones.extend(('Dino', 'Happy'))

# 9. Return a new version of this sentence that ends just before the word house. Don't worry about spaces
# or punctuation: remove everything starting from the beginning of house to the end of the sentence.
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected return value:
# => 'Few things in life are as important as
# answer 1
advice.split('house')[0]
# answer 2
index_house = advice.find('house')
print(advice[:index_house])

# 10. Replace the word "important" with "urgent" in this string:
advice = "Few things in life are as important as house training your pet dinosaur."
# answer
advice.replace('important', 'urgent')
