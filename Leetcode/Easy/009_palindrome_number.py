class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str_reg = str(x)          # regular order of digits
        x_str_rev = str(x)[::-1]    # reversed order of digits using string slicing in python

        if x_str_reg == x_str_rev:
            return True
        else:
            return False
        

# SOLUTION LINK: https://leetcode.com/problems/palindrome-number/post-solution/?submissionId=1499588563
