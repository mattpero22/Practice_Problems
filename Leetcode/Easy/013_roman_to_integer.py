class Solution:
    def romanToInt(self, s: str) -> int:
        numeral_values: dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum: int = 0
        prev_numeral: str = ""

        for numeral in s:
            # if the previous is less than the current, we need to subtract twice its value from the current before adding to undo the previous addition of that numeral value
            if (prev_numeral != "" and (numeral_values[prev_numeral] < numeral_values[numeral])):                
                sum += numeral_values[numeral] - 2 * numeral_values[prev_numeral]
            else:
                sum += numeral_values[numeral]

            prev_numeral = numeral

        return sum


# SOLUTION LINK: https://leetcode.com/problems/roman-to-integer/post-solution/?submissionId=1503163330
