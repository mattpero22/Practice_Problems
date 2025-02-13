# PROBLEM: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    print(word)
    characters_detected = {}
    result = ''
    for ch in word:
        current = ch.lower()
        if current in characters_detected:
            characters_detected[current] += 1
        else:
            characters_detected[current] = 1
            
    for ch in word:
        current = ch.lower()
        if characters_detected[current] > 1:
            result += ")"
        else:
            result += "("
    
    return result