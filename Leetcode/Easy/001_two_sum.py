from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] + nums[j] == target:
                    return [nums[i], nums[j]]
        
        return None
                

# SOLUTION LINK: https://leetcode.com/problems/two-sum/post-solution/?submissionId=1499024397   (1/5/2025)


class Solution2:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        previous: dict = {}

        for i in range(len(nums)):
            match = target - nums[i]
           
            if (match in previous):
                return [previous[match], i]
            else:
                previous[nums[i]] = i
        
# Went back to solve with hash map instead of two loops and to ensure I understood problem from the other day.
#SOLUTION2 LINK: https://leetcode.com/problems/two-sum/post-solution/?submissionId=1503450092 (1/9/2025)