from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] + nums[j] == target:
                    return [nums[i], nums[j]]
        
        return None
                

# SOLUTION LINK: https://leetcode.com/problems/two-sum/post-solution/?submissionId=1499024397   (1/5/2025)
        