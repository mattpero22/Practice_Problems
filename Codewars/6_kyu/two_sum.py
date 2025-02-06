'''
PROBLEM: 

Plan of Attack:
    use a hash map to track items we have seen in the given array.
    while we iterate, find the complement of the current number and then check if we have encountered it.
'''

def two_sum(numbers, target):
    matches = {}
    for i in range(0, len(numbers)):
        match = target - numbers[i]
        if match in matches:
            return (i, matches[match])
        else:
            matches[numbers[i]] = i

    return None

'''
COMPLETED: 10 minutes

solid solution using hashmap
time complexity: O(n)
space complexity: O(n)
'''