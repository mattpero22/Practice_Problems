# PROBLEM: https://www.codewars.com/kata/5679aa472b8f57fb8c000047

def find_even_index(arr):
    i = 0
    while i < len(arr):
        l_sum = 0
        r_sum = 0
        
        for l in range(0,i):
            l_sum += arr[l]
        
        for r in range(i+1,len(arr)):
            r_sum += arr[r]
        
        if l_sum == r_sum:
            return i
        i += 1
        
    return -1