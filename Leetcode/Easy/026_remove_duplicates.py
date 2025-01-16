from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[next] = nums[i]
                next += 1

        return next


# SOLUTION: https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/6290074/modify-inplace-by-mattpero22-cbdj/