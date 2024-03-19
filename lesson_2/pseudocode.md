# a function that returns the sum of two numbers

    *Informal*
    Given two numbers a and b
    add a to b and save the value to variable called total
    return total
        
    *Formal*
    START
    SET total = 0
    total = a + b
    return total
    END
    
# a function that takes a list of strings, and returns a string that is all those strings concatenated together

    *Informal*
    Given a list of strings my_strings
    Create an empty string called new_string
    Iterate through each string in my_strings
        - Concatenate the current string to new_string
    return new_string
    
    *Formal*
    START
    Given a list of strings called my_strings
    SET new_strings = ''
    SET iterator = 0
    while iterator < lengths of my_strings
        new_strings = new_strings + element within my_strings at space "iterator"
        iterator = iterator + 1
    return new_strings
    END
    
# a function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element. For instance:
# every_other([1,4,7,2,5]) # => [1,7,5]

    *Informal*
    Given a list of integers called original_list
    Create an empty list called new_list
    Iterate through original_list by index
        If the index is even, add the element at the current index to new_list.
    return new_list

    *Formal*
    START
    Given a list of integers called original_list
    SET new_list = []
    SET iterator = 0
    while iterator < lengths of original_list
        if iterator is even
            add original_list[iterator] to new_list
        increment iterator by 1
    return new_list
    END
    
# a function that determines the index of the 3rd occurrence of a given character in a string. For instance, if the given character is 'x' and the string is 'axbxcdxex', the function should return 6 (the index of the 3rd 'x'). If the given character does not occur at least 3 times, return None.

    *Informal*
    Given a string called my_string
    Given a character called given_character
    Create a variable called occurence with starting value 0
    Iterate through the character of my_string
        if current character is the same with given_character
            increment occurence by 1
            if occurence equals 3, return the index of current character
        If the character does not occur at least 3 times, return None.
        
    *Formal*
    START
    Given a string called my_string
    Given a character called given_character
    SET occurence = 0
    SET index = 0
    while index < length of my_string
        if my_string[index] equals given_character
            increment occurence by one
            if occurence equals 3
                return index
        Increment index by one
    return None
    END
    
# a function that takes two lists of numbers and returns the result of merging the lists. The elements of the first list should become the elements at the even indexes of the returned list, while the elements of the second list should become the elements at the odd indexes. For instance:
# merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]
# You may assume that both list arguments have the same number of elements.

    *Informal*
    Given two lists list_1 and list_2
    Create an empty list called new_list
    Create a variable index with value set to 0
    Iterate through index up to length of list1 or list2
        - add list1 at space 'index' to new_list
        - add list2 at space 'index' to new_list
        - increment index by 1
    return new_list

    *Formal*
    START
    Given two lists list_1 and list_2
    SET new_list = []
    FOR index from 0 to length of list1 or list2
        append list1[index] to new_list
        append list2[index] to new_list
    END FOR
    return new_list
    END

    

