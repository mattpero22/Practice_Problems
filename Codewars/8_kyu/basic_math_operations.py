'''
Problem: https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Plan:
function will take in the operation as a str and two values as seperate arguments. Return the result based on the operation.

1. detect which math operation was passed to the function
2. return the operation performed as num 1 (OPERATION) num2

only 4 cases so simple if else is good.
'''

def basic_op(operator, value1, value2):
    if operator == '+': return value1 + value2
    elif operator == '-': return value1 - value2
    elif operator == '*': return value1 * value2
    elif operator == '/': return value1 / value2

'''
Comments:
    * COMPLETED: simple practice problem (5 min)
    * time complexity
        * worst case, '/' where it would be 4 conditional checks to return a result.
        * there are a finite number of operations/checks thus the result is of O(1) or essentially constant for all inputs.
'''

