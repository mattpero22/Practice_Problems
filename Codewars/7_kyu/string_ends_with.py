'''
Problem: https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python

Instructions:
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string). 
'''

def solution(text, ending):
    return text[len(text) - len(ending):] == ending
    


if __name__ == '__main__':
    text = 'samurai'
    ending = 'ai'
    print(solution(text, ending))

    

'''
Notes:
    # first test case works, but hits and error if there is more than one instance of ending when using .index().
    # changed it to return the comparison of the text's last 'n' chars to the ending passed in, where n is the number of characters in the ending.
Result:
    COMPLETED: 10 min
'''