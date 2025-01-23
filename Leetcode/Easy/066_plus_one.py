from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(d) for d in digits]
        number = "".join(digits)
        number = str(int(number) + 1)
        digits = [int(d) for d in number]
        return digits
    


#SOLUTION: https://leetcode.com/problems/plus-one/solutions/6321605/plus-one-python-by-mattpero22-r3zi/