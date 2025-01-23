from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0

        l = 0
        h = len(nums) - 1
        while (l <= h):
            mid = int((l + h) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1

        return l
    
# SOLUTION: https://leetcode.com/problems/search-insert-position/solutions/6320130/binary-search-by-mattpero22-qxpw/