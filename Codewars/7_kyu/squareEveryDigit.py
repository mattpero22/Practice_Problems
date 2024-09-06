'''
Problem: https://www.codewars.com/kata/546e2562b03326a88e000020/train/python

Instructions:
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
'''

def squareEveryDigit(num):
    num_str = str(num)
    digits = [int(digit) for digit in num_str]
    squares = [str(digit ** 2) for digit in digits]
    return int("".join(squares))


if __name__ == '__main__':
    num = 9119
    print(squareEveryDigit(num))
    

'''
Notes:
    Had to be careful with type conversions in order to use string methods along with math on the digits

    Used for loops to generate the necessary arrays in a pythonic way

COMPLETED: 10 minutes
'''