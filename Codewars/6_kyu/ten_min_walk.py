'''
Problem: https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

In my words:
    Given an array of direction characters, determine if it is a valid 10 minute walk
    Each character represents 1 block of walking in that direction
    each block takes 1 minute
    must return to starting point
    can not be early or late for the 10 minute walk

Assumptions:
    will not receive empty array
    will always receive valid characters of n s w e in their lowercase format

Plan of attack
    * check length of the walk, if it is not equal to 10, it can never be a 10 minute walk
    * define a coodinate system start point of x=0 and y=0, perhaps as single list -> pos = [0,0]
    * iterate through our directions and create a case for each direction
        * if n -> y + 1
        * if s -> y - 1
        * if e -> x + 1
        * if w -> y + 1
            as per a standard cartesian definition
    * Check if position is 0,0
        * if it is, then return True for valid walk
        * otherwise return False as we do not return to start

'''

def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        pos = [0,0]
        for direction in walk:
            if direction == "n":
                pos[1] += 1
            elif direction == "s":
                pos[1] -= 1
            elif direction == "e":
                pos[0] += 1
            elif direction == "w":
                pos[0] -= 1
        
        if pos != [0,0]:
            return False
        else:
            return True

'''
COMPLETED: 14 minutes

THOUGHTS:
    * looking at other kata solutions, there were crafty one -liners that used each condition in a logical evaluation
        for example in psuedo code:
        return the evaluation of
            length of walk is 10 exactly AND we go north the same amount as south AND we go east the same amount as we go west
        And the top variation in Python for this kata:
            def isValidWalk(walk):
                return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
        
TIME COMPLEXITY
    * we do a single check on the length of the input using len() -> O(1)
    * iterate through each element of the given walk array -> O(n) where n is length of walk
    * worst case would be 4 logical checks to get to 'w', and then the arithmetic so O(5) within loop which is -> O(1)
    * one more logical check to see if we are back at the beginning -> O(1)

    O(1) + O(n) + O(1) -> O(n)

        -- we know for this specific problem a walk will probably not be that long and for 99% of tests will likely be something like O(10) -> constant speed
        -- a thought to keep in mind when designing for a real world solution, as if it does not need to be super fancy to make it faster, keep it simple

'''