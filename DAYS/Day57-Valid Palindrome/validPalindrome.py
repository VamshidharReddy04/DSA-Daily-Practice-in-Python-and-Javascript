# Strings - Valid Palindrome Leetcode 125
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Example 1: Input: s = "A man, a plan, a canal: Panama" Output: true
# Example 2: Input: s = "race a car" Output: false

# Different Approaches:
# 1. String Reversal- Time O(n), Space O(n)
# 2. Two Pointers- Time O(n), Space O(1)
# Leetcode: https://leetcode.com/problems/valid-palindrome/
# Solution:
import re  # re is used for regular expression operations
def validPalindrome(s):
    cleaned=re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    l=0
    r=len(cleaned)-1
    while l<r:
        if cleaned[l]!=cleaned[r]:
            return False
        l+=1
        r-=1
    return True
# Test Cases
print(validPalindrome("A man, a plan, a canal: Panama"))  # True
print(validPalindrome("race a car"))  # False
# Two Pointers Approach :
def validPalindromeTwoPointers(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
print(validPalindromeTwoPointers("A man, a plan, a canal: Panama"))  # True 
print(validPalindromeTwoPointers("race a car"))  # False    


# Best Approach: Two Pointers
# Complexity Analysis: Time Complexity: O(n), Space Complexity: O(1)
