'''
Problem: https://www.codewars.com/kata/58649884a1659ed6cb000072/train/python
Instructions:
    Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

Plan of Attack:
    1. get the input as the current light color
    2. store the next steps as a dictionary {current:next}
    3. access dictionary using key of current light color and return its next value using access by key name
'''

def update_light(current):
    traffic_light_flow = {
        'green': 'yellow',
        'yellow': 'red',
        'red': 'green'
    }
    return traffic_light_flow[current]

'''
COMPLETED: 3 minutes
Time Complexity:
    * O(1) -> simply accessing a dictionary with a key (akin to hash table access) and returning its value
'''