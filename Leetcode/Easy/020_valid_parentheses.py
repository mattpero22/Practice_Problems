class Solution:
    def isValid(self, s: str) -> bool:
        parentheses, squares, curlys = 0, 0, 0
        next_close_expected = []
        complements = {"(":")", "[":"]", "{":"}"}

        for char in s:
            if char in "([{":
                next_close_expected = [complements[char]] + next_close_expected
            if char in ")]}":
                if len(next_close_expected) == 0 or char != next_close_expected[0]:
                    return False
                next_close_expected.pop(0)
            
            if char == "(": parentheses += 1
            elif char == ")": parentheses -= 1
            elif char == "[": squares += 1
            elif char == "]": squares -= 1
            elif char == "{": curlys += 1
            elif char == "}": curlys -= 1

        return parentheses == squares == curlys == 0
    
# SOLUTION LINK: https://leetcode.com/problems/valid-parentheses/solutions/6285097/valid-parentheses-take-1-by-mattpero22-qn9q/
