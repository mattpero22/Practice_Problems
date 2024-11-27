'''
Problem: https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

Objective: 
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.


Gameplan/Plain English Solution:
1. Create our empty object to store the return set
2. Check if the given string has length, and if not return the empty set
3. Otherwise, iterate through the given string one char at a time
4. Within the iteration, use key:value notation to store the current char as the key
5. Check if the key for the current character exists and if it does skip adding a new key and add one to value
6. Increment the value of the key for the specific character
7. Repeat for length of string
8. Return dictionary of {character: occurrences}

'''

def counting_chars(s):
    character_count = {}
    if len(s) > 0:
        for char in s:
            if char in character_count:
                character_count[f"{char}"] += 1
            else:
                character_count.update({f"{char}":1})

        return character_count
    else:
        return {}


'''
COMPLETED: 
    10 minutes
Comments:
    * had to look up how to check a key existing properly, was going to use dict.keys uneccessarily
    * time complexity
        - checking the length of string (n)
        - checking the length is constant for each given string -> O(1)
        - For loop has max iterations of the length of string n -> O(n)
        - Looking up a key in python is O(1) as is updating the dictionary within the if/else check
        - Thus, we have O(1) x O(n) which simplifies to O(n)
'''
