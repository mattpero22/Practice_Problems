'''
Problem: https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python

Instructions:
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

"This is an example!" ==> "sihT si na !elpmaxe"
'''

def reverse_words(text):
    words = text.split(' ')
    rev = []
    print(words)
    for word in words:
        # handle double space
            rev.append(word[-1:-(len(word)+1):-1])
    return " ".join(rev)


if __name__ == '__main__':
    text = 'double  spaces'
    print(reverse_words(text))

'''
Notes:
    # good exercise in iterating through text in reverse, realize I could have made it simpler by doing words[::-1] rather than the math I chose in my solution.

    # could have simplified my if else and simply appended each time. The 'join' string method would have handled the double space


Result:
    COMPLETED: 10 minutes
'''