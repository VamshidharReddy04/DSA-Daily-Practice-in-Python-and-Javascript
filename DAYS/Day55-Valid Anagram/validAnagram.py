# String - Valid Anagram leetcode 242
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1: Input: s = "anagram", t = "nagaram" Output: true
# Example 2: Input: s = "rat", t = "car" Output: false

# Different Approaches:
# 1. Sorting both strings and comparing the sorted versions- Time O(n log n), Space O(1)
# 2. Frequency counting - Time O(n), Space O(1)
# Leetcode https://leetcode.com/problems/valid-anagram/

# Sorting both strings and comparing the sorted versions
from collections import Counter as counter
def isAnagrams(s:str,t:str)->bool:
    if len(s)!=len(t): return False
    return counter(s)==counter(t)
# Test cases
print(isAnagrams("anagram", "nagaram"))  # True
print(isAnagrams("rat", "car"))          # False
print(isAnagrams("listen", "silent"))    # True

# Frequency counting 
def isAnagram(s:str,t:str)->bool:
    if len(s)!=len(t): return False
    count=[0]*26
    for char in s:
        count[ord(char)-ord('a')]+=1
    for char in t:
        count[ord(char)-ord('a')]-=1
    for c in count:
        if c!=0:
            return False
    return True
# Test cases
print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))          # False
print(isAnagram("listen", "silent"))    # True

# Best Approach: Frequency counting 
# Complexity Analysis: Time complexity: O(n), Space complexity: O(1)