'''
Problem: https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.


Objective: When given a string as input, determine if it is a pangram and return True if so. Otherwise return False.

Gameplan/Plain English Solution:
1. set the string to lowercase to handle both caps and lowers
2. iterate through the alphabet
3. iterate through the given string until we find current letter
4. if we find the current letter, then go to next iteration of alphabet
5. if we do not find the current letter, we want to return False as the given is not a pangram.
6. if we get through all letters of the alphabet, return True

'''

def is_pangram(st):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    st = st.lower()

    for letter in alphabet:
        if not letter in st: 
            return False

    return True

'''
COMPLETED: 25 min

Comments:
    * happy with this solution as it is pretty straightforward to read
    * time complexity is (26 * n) + (1 * n) where n is the number of characters in the string input
        * 26 * n for iterating through 'n' characters for each letter of alphabet
        * 1 * n for the conversion from input to lowercase string (assumption of 1 process per char for the conversion)
        * 26n + n = 27n
    * thus, dropping constants, this solution has a time complexity of O(n)
'''



