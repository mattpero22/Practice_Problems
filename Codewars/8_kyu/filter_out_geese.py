# PROBLEM: https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    i = 0
    while i < len(birds):
        if birds[i] in geese:
            birds.pop(i)
        else:
            i += 1
            
    return birds