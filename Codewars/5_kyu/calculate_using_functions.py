'''
PROBLEM: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

IN MY WORDS:
    * write calculations using only functions and their results
        ie: seven(times(five())) -> yields 35
    * each digit has a function (0-9)
    * each mathematical operation must have a function
    * outer function is the left operand
    * inner function is the right operand
    * do integer division not float
        
PLAN OF ATTACK:
    1. Define a function for each digit that returns its value, and optionally can accept an operation as a param
    2. Return an abstract function from each operation using a lambda to transfer the input "num" back to the initial number functions
    3. Once the lambda is returned in the first number function, it can evaluate by adding its digit into the lambda in place of x
'''
def zero(op=None):
    return op(0) if op else 0
def one(op=None): 
    return op(1) if op else 1 
def two(op=None):
    return op(2) if op else 2 
def three(op=None):
    return op(3) if op else 3
def four(op=None):
    return op(4) if op else 4
def five(op=None):
    return op(5) if op else 5
def six(op=None):
    return op(6) if op else 6
def seven(op=None): 
    return op(7) if op else 7
def eight(op=None):
    return op(8) if op else 8
def nine(op=None):
    return op(9) if op else 9

def plus(num): return lambda x: x + num
def minus(num): return lambda x: x - num
def times(num): return lambda x: x * num
def divided_by(num): return lambda x: x // num


'''
RESULTS: COMPLETED (30 min)
    * had to look up and refresh my memory on lambda and *args for the optional parameters in this problem

TIME COMPLEXITY:
    O(1) max 3 operations
SPACE COMPLEXITY:
    O(1) need a register for each digit and each operation, as well as temporary memory for the return statements used as parameters
'''