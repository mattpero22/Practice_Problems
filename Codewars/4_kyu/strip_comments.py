'''
Problem:
https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

Instructions:
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples

The output expected would be:

apples, pears
grapes
bananas
'''

def strip_comments(string, markers):
    str_arr = str(string).split("\n")

    for idx, line in enumerate(str_arr):
        for char in line:
            if char in markers:
                marker_pos = line.index(char)
                str_arr[idx] = str_arr[idx][0:marker_pos].rstrip()

    return "\n".join(str_arr)

if __name__ == '__main__':
    string = "apples, pears # and bananas\ngrapes\nbananas !apples"
    markers = ["#", "!"]
    print(strip_comments(string, markers))


'''
Notes:
    double iteration to go through each line, then each character in the line

    ran into hiccup with the removal of whitespace from after the marker only and leaving the beginning of the commented line alone
        had to use rstrip() rather than strip()

COMPLETED: 15 minutes
'''