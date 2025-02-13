'''
PROBLEM: https://www.codewars.com/kata/5865918c6b569962950002a1
'''

def str_count(strng, letter):
    count = 0
    for ch in strng:
        if ch == letter:
            count += 1
    
    return count