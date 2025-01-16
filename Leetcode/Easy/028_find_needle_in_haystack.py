class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        for i in range(0, len(haystack)):
            if haystack[i] == needle[0]:
                counter = 0
                for j in range(0, len(needle)):
                    if i+j < len(haystack):
                        if haystack[i+j] == needle[j]:
                            counter += 1
                            if counter == len(needle):
                                return i
                        else:
                            break

        return -1

#SOLUTION: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/6291143/find-needle-in-haystack-by-mattpero22-2pwq/