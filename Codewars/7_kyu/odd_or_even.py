# PROBLEM: https://www.codewars.com/kata/5949481f86420f59480000e7

def odd_or_even(arr):
    sum = 0
    
    for num in arr:
        sum += num
    
    if sum % 2 == 0:
        return "even"
    else:
        return "odd"