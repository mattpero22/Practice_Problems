'''
Problem:https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

Instructions:
    Your job is to write a function which increments a string, to create a new string.
        If the string already ends with a number, the number should be incremented by 1.
        If the string does not end with a number. the number 1 should be appended to the new string.

Plan of Attack:
    1. Check for the trivial case, where the last character is an alphabet and not a digit
    2. If it is not, simply add the char '1' to end of string and return
    3. Otherwise, go through the string from back to front until we get an alphabetic character
    4. Once we get the location of the highest index alphabet character, we can take from that index to the end of string to get the number to increment
    5. Splice the number out of the string and convert to a Number/Integer
    6. Add one to the number and then concatenate to the end of the string

'''

def increment_string(strng):
    steps_to_alpha = None
    if strng == "":
        strng = "1" 
    elif strng[-1].isalpha():
        strng += '1'
    else:
        for i,char in enumerate(reversed(strng)):
            if char.isalpha():
                steps_to_alpha = i
                break
        
        splice_start = len(strng) - steps_to_alpha
        ending_number = strng[splice_start:]
        if '.' in ending_number:
            ending_number = str(float(ending_number) + 1)
        else:
            ending_number = str(int(ending_number) + 1)
        
        while (len(ending_number) < steps_to_alpha):
            ending_number = '0' + ending_number


        strng = strng[:splice_start] + ending_number

        print(strng)

    return strng

'''
Solution failed when given a string of only numbers

could have used this simple solution, as another reason I stopped was my code is getting too complex and would need a rework
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

    totally forgot about rstrip and such 
'''