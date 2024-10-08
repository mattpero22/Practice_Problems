'''
Problem: https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
Instructions: 
    1. sort a given string where each word has their position stored as a number within the word (o1ne pla2ce t3o go4...)
    2. Numbers start counting from 1
    3. If input is empty return empty

Solution1 (Trivial):
    1. start at 1, and iterate through the words until you find our target number
    2. take word where target number was found and add to our return string
    3. increment the target and look for next word with the target number
    4. if target is not found return our return string
'''

def order(sentence):
    ret_str = ''
    target = 1
    arr_sentence = sentence.split(' ')

    while target <= len(arr_sentence):
        for word in arr_sentence:
            for char in word:
                if char == target:
                    if len(ret_str) > 0: ret_str += " "
                    ret_str += word

        target += 1

    return ret_str


'''
Notes:

Result:

'''