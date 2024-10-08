'''
Problem: https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
Instructions:
    1. count the number of True statements in given array
'''

def count_sheep(sheep):
    count = 0
    for sheep in sheep:
        if sheep: count += 1
    
    return count

'''
Notes:
    * time complexity is O(n) because we need to iterate through the given array one time to get our result

Result:
    Completed (2min)
'''