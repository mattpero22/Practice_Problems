from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k    

#SOLUTION: https://leetcode.com/problems/remove-element/solutions/6291078/remove-element-in-place-by-mattpero22-86vf/

