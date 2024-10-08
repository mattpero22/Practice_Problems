'''
Problem: https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python
Instructions:
    1. write a function that takes a list of strings as input.
    2. return a list of each string with the proper number preceding it
    number starts as 1

'''

def number(lines):
    ret_arr = [f'{idx + 1}: {line}' for idx, line in enumerate(lines)]
    return ret_arr

'''
Notes:
    * n operations to enumerate (n)
    * n operations to iterate through and append (Constant * n)
    * simplest form time complexity would be O(n)
Result:
    COMPLETED (5 min)
'''
