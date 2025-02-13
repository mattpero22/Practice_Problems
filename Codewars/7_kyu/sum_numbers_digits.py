# PROBLEM: https://www.codewars.com/kata/52f3149496de55aded000410

def sum_digits(number):
    sum = 0
    num = str(number)
    
    if num[0] == '-':
        num = num[1::]
        
    for digit in num:
        sum += int(digit)
        
    return sum