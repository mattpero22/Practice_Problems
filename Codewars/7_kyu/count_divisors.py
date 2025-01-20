'''
Problem: https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/python

1. iterate through all numbers from 1 to sqrt(n)
2. find modulus/remainder of divsion for n/i
3. if remainder is 0, add to the count
4. otherwise continue as usual

'''
def divisors(n):
    d = []
    count = 0
    for i in range(1,round(pow(n,.5)) + 1): # go from 1 to the squareroot of n to reduce iterations
        q = n/i
        if n % i == 0:
            count += 2
            if q == i:
                count -= 1

    return len(d)


'''
RESULTS: 15 minutes

Time complexity: O(√n)
* by iterating only up to the square of the given number we reduce the iteration range by a significant amount from n to its sqrt()
* perform constant operations within the loop, evaluating quotients and remainders and appending to a list
* at the end we have a list with the size equal to number of unique divisors


Space complexity: O(1)
* need to define an iterator and a counter variable only in memory, which takes constant space. no dynanic data types needed.


'''
