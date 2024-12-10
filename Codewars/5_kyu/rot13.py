'''
Problem: https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
    - takes in a string and returns the string ciphered under ROT13
    - ignore numbers and special characters
    - dont use encode

Assumptions:
    * Given
        - assume we are getting a string in english/latin alphabet characters
        - all other characters can be ignored and returned as is

    * Own
        - assume all inputs are length > 0

Plan of Attack:
    * create a palceholder string to store our return chars
    * iterate through each character of the given string
    * for each one, check if it is an alphabet character
    * if it is an alphabet character convert to an int, add its ASCII char value +13 to our return string
        * must be mindful of the character limits for ASCII, as in z and Z are the max values possible
    * if it is not an alphabet, add the character to our return string as is
    * return the string once all characters have been iterated over
'''

def rot13(message):
    cipher = ''
    lower_int_limit = 0
    upper_int_limit = 0

    for ch in message:
        if ch.isalpha():
            if ch.islower():
                lower_int_limit = ord('a')
                upper_int_limit = ord('z')
            elif ch.isupper():
                lower_int_limit = ord('A')
                upper_int_limit = ord('Z')

            cipher_char = ord(ch) + 13

            if cipher_char > upper_int_limit:
                rem = cipher_char - upper_int_limit
                cipher_char = lower_int_limit + rem - 1
                cipher += chr(cipher_char)
            else:
                cipher += chr(cipher_char)

        else:
            cipher += ch
    
    return cipher


'''
COMPLETED: 30 minutes

Time Complexity Analysis:
    * setting up storage variables -> constant
    * iterate through each character in the message. This takes 'n' times where n is the length of the string.
    * check if it is alphanumeric -> constant
    * check if it is upper or lower -> constant
    * assign limits -> constant
    

    all constant checks and operations inside of the for loop -> O(n)

''' 




