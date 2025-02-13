#PROBLEM: https://www.codewars.com/kata/5266876b8f4bf2da9b000362

def likes(names):
    res = ''
    if len(names) == 0:
        res = 'no one likes this'
    if len(names) == 1:
        res = f'{names[0]} likes this'
    if len(names) == 2:
        res = f'{names[0]} and {names[1]} like this'
    if len(names) == 3:
        res = f'{names[0]}, {names[1]} and {names[2]} like this'
    if len(names) >= 4:
        res = f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
        
    return res