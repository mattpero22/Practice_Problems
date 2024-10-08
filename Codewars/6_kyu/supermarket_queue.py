'''
Problem: https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python
Instructions: 
    1. calculate total time required for all customers to checkout
    2. given an array of customers, where each value is the amt of time needed to checkout
    3. given the number of checkout stations

Plan of Attack:
    1. Look at the list of customers and number of till
    2. create a timer for each till
    3. Assign customer to the till with the lowest timer
    4. repeat for all tills
    5. once through with all customers, return the highest till timer
'''

def queue_time(customers, n):
    till_queues = [0 for i in range(0,n)]
    for customer in customers:
        lowest_time = min(till_queues)
        available_till = till_queues.index(lowest_time)
        till_queues[available_till] += customer

    return max(till_queues)

'''
Time Complexity:
    let m = number of customers
    let n = number of tills

    O(1) * n operations to create the tills array = O(n)
    m iterations with k operations for the customer
    where k = ... 
        O(n) to find lowest till
        O(n) to find the index of lowest till
        O(1) to update index

    O(m*k) -> O(m*(2n)) -> O(2mn)
    simplifies to: O(m*n)

    
Results:
    Completed 10 minutes
'''