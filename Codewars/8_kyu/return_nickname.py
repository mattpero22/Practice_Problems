'''
Problem: https://www.codewars.com/kata/578c1e2edaa01a9a02000b7f/train/python

uses preloaded dictionaries FIRSTNAME AND SURNAME

'''


def alias_gen(f_name, l_name):
    if f_name[0].isnumeric() or l_name[0].isnumeric():
        return 'Your name must start with a letter from A - Z.'
    
    return FIRST_NAME[f_name[0].upper()] + " " + SURNAME[l_name[0].upper()]