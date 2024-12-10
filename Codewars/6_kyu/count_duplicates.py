'''
Problem: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

In my own words:
    * write a function that detects numbers and letters that occur more than once
    * if a character does occur more than once, return the number of characters with duplicates

Assumptions:
    * contains only alphabet and numeric characters

Plan of Attack:
    * create a dictionary to store our counts of each letter/number\
    * force the string to lowercase as the instructions say case insensitive
    * iterate through string
    * if the character is a number, access our dictionary and add 1
    * if the character is a letter, convert it to lower
     
'''

def duplicate_count(text):
    counter = {}
    text = text.lower()
    for char in text:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1  

    counter_dupes = {key:value for key,value in counter.items() if value > 1}

    return len(counter_dupes.items())

'''
COMPLETED: 25 minutes

TIME COMPLEXITY:
    * iterate through n times where n is length of the given text
        * perform constant operations (look up and update value, convert to lower) within the loop
    * iterate through our counter dictionary (up to n - number of duplicates iterations)
        * worst case would be no duplicates so the second iteration would also be O(n)

    overall O(n)

'''