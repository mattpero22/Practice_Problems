'''
Problem: https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Restate problem and Plan of attack:
    * takes a non-negative integer (int) and returns the digits in descending order (int)
        1. split the input number into its digits
        2. use python.sort to sort them in ascending order
        3. iterate through the list backwards to create a list of digits from highest to lowest
        4. join the digits
        5. cast as int
        6. return
'''

def descending_order(num):
    digits = [d for d in str(num)]
    digits.sort()
    descend_digits = [d for d in digits[::-1]]
    descend_digits = ''.join(descend_digits)
    return int(descend_digits)


descending_order(123456789)

'''
    Notes: COMPLETED (10 minutes)
    Time Complexity:
        (let 'n' = the length of the input number)
        # converting the digits to a list would have 'n' operations
        # sorting the digits list using python's 'sort'  would also have 'n' operations (at least, + C where C is a random number of iterations)
        # generating a list of the digits descending also has 'n' operations
        # lastly, joining them together for the return string gives a final 'n' operations
        # thus the time complexity is '4n + C'  or simply O(n) when constants are dropped
'''