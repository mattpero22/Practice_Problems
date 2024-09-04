# Problem Instructions
'''
Problem: https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG

Instructions:
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.
'''


def increasingSequence(sequence):
    ctr = 0
    pop_ctr = 0
    
    while ctr < len(sequence):
        if pop_ctr <= 1:
            try:
                if sequence[ctr] < sequence[ctr + 1]:
                    ctr += 1
                    continue
                else:
                    sequence.pop(ctr + 1)
                    pop_ctr += 1
                    if ctr == 0: ctr += 1
            except IndexError:
                break
        else:
            return False
        
    return True        


def solution(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        print(f'elm:{elm}, last:{last}, prev:{prev}', droppped)
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True

if __name__ == '__main__':
    test_sequence = [10,1,2,3,4,5]
    #print(increasingSequence(test_sequence))
    print(solution(test_sequence))

# Notes/Thoughts
'''
Notes:
    Effective way of handling the IndexError for the iteration on the final element was to use the "try, except" block

    Switched to a while loop as the logical flow made more sense. I typically try to use a for loop before resorting to while.

    Ran into issue on test where the first number (index 0) was larger than the rest. Tried to rework it a couple ways but got stuck. 

INCOMPLETE: 45min
'''

#Solution
'''
Top Solution:
https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG/solutions?solutionId=bTfqJKMjXiT7PYa8C

def solution(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True

In my own words:
    we have a flag called droppped initially set to false and set two variables equal to less than the minimum value of the given sequence. last and previous keep track of values we have checked in the list.

    on each iteration, we check if the current number (elm) is <= the last number. if it is not, we update prev and last to be the items previously checked in the sequence.

    if elm is less than the last number, we have hit an issue, and check if it is the first or second occurrence. If it is the second time, we return false for an invalid sequence. if elm is <= prev, update prev to be the same value as last to handle the current element. Otherwise, we are good to go and the sequence is increasing.

'''