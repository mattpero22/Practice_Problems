class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        array = s.strip().split(" ")
        return len(array[-1])
    
# SOLUTION: https://leetcode.com/problems/length-of-last-word/solutions/6320449/pythonic-last-word-length-by-mattpero22-tjk0/