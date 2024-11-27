'''
Problem: https://www.codewars.com/kata/563f037412e5ada593000114/train/python

Your task is to complete the method provided and return the number of years 'Y' as a whole in order for Mr. Scrooge to get the desired sum.

Assumption: Assume that Desired Principal 'D' is always greater than the initial principal. However it is best to take into consideration that if Desired Principal 'D' is equal to Principal 'P' this should return 0 Years.

Restate problem and Plan of attack:
    1. Check that desired principle D is greater than the initial principal
    2. If it is, we will have to go year by year, calculating the interest, tax, and computing the remaining investment
    3. Once investment for the year has be calculated, compare to the desired amount, D
    4. If investment account >= D, return the number of iterations (years = Y)

'''

def calculate_years(principal, interest, tax, desired):
    Y = 0
    print(principal, interest, tax, desired)
    if desired > principal:
        while (principal <= desired):
            Y += 1
            yearly_gain = (principal * interest)
            yearly_tax = (yearly_gain * tax)
            yearly_net = yearly_gain - yearly_tax
            principal += yearly_net

    return Y



'''
    Notes: COMPLETED (15 minutes)
        * happy with my solution as I kept it clear, with one operation per line for an easily readable method
    
    Time Complexity:
        * BEST case is O(1) where the desired is less than or equal to the principal
        * Otherwise, we would have to iterate the while loop as many times as needed to get to the desired, let that be 'n' times
        * within each iteration of the while loop, we are doing 4 arithmetic operations with O(1), totaling 4*O(1) and reduced simply to O(1)
        * thus we are performing O(1) operation time complexity up to n times for a total worst case of O(n)

        ^^^^^^^^^^^^ WRONG!, explanation for time complexity below ^^^^^^^^^^^^^^^^^

        * yearly_net = (P * I) - (P * I * T) = P * I * (1 - T)
        * principal_n = principal_0 * (1 + I * (1 - T))^n
        * log()(principal_n) = log()(principal_0) * n
        n = log()(principal_n / principal_0) 

        thus the number of iterations n is equal to the log of the ratio between our desired(principal after n iterations) and our initial

        O(n) = O(log()((principal_n / principal_0)))
'''