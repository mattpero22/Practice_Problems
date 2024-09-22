'''
Problem: https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expandedForm(12)    --> should return "10 + 2"
expandedForm(42)    --> should return "40 + 2"
expandedForm(70304) --> should return "70000 + 300 + 4"
NOTE: All numbers will be whole numbers greater than 0.

Plan:
    1. convert the number given into a string
    2. split each of the digits up
    3. iteratre through each digit and add it to the return string
    4. if the digit is zero, skip to next iteration
    5. detect what index the current digit is, and add the required amount of zeroes onto the ret string
    6. if it is the last digit, return, otherwise, add a ' + ' to delimit each expanded term

    * a way to detect the correct number of zeroes would be to take the len of the num 'L' and calculate L - (index + 1)
        * 456 = 400 + 50 + 6
            L = 3
            for 4 -> index = 0
            3 - (0 + 2) = 1 zero
        * we add + 1 to overcome zero-indexing
'''

def expanded_form(num):
    str_num = str(num)
    str_ret = ''
    position = 0

    for digit in str_num:
        if digit != '0':
            zeroes = (len(str_num)-(position + 1)) * '0'
            str_ret = str_ret + f'{digit}{zeroes}'
            if position != len(str_num)-1:
                str_ret += ' + '
        elif digit == '0' and position == len(str_num)-1:
            str_ret = str_ret[:-3]  

        position += 1

    return str_ret

print(expanded_form(6090400))

'''
Notes:
    # Results: COMPLETED 30 minutes
    # time complexity:
        let n = length of our num parameter
        n iterations for the number where we perform a constant number of logical/computational operations
        thus the complexity would be C * n, or in simplest form, O(n). 
        the limiting factor would be the number of digits to iterate through
'''