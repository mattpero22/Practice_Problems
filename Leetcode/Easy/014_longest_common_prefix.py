from typing import List

def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):
        for string in strs:
            if i == len(string) or string[i] != strs[0][i]:
                return strs[0][:i]
    
    return strs[0]


test0 = [""]
test1 = ["dog", "racecar", "time"] 
test2 = ["apple", "ape", "alpine"]
test3 = ["flowers", "flow", "flight"]
test4 = ["dog", "doubt", "dung", "fox"]

print("Test0 Longest Common: ", longestCommonPrefix(test0), "\n")
print("Test1 Longest Common: ", longestCommonPrefix(test1), "\n")
print("Test2 Longest Common: ", longestCommonPrefix(test2), "\n")
print("Test3 Longest Common: ", longestCommonPrefix(test3), "\n")
print("Test4 Longest Common: ", longestCommonPrefix(test4), "\n")