# PROBLEM: https://www.codewars.com/kata/583f158ea20cfcbeb400000a

def arithmetic(a, b, operator):
    add = lambda a,b: a + b
    sub = lambda a,b: a - b
    mul = lambda a,b: a * b
    div = lambda a,b: a / b
    
    if operator == "add":
        return add(a,b)
    elif operator == "subtract":
        return sub(a,b)
    elif operator == "multiply":
        return mul(a,b)
    elif operator == "divide":
        return div(a,b)
    
