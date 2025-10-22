# Strings- Palindrome Substring Leetcode 647
# Given a string s, return the number of palindromic substrings in it.
# Example 1: Input: s = "abc" Output: 3
# Example 2: Input: s = "aaa" Output: 6

# Different Approaches:
# 1. Brute Force Approach: Time O(N^3) Space O(1)
# 2. Dynamic Programming Approach: Time O(N^2) Space O(N^2
# 3. Expand Around Center Approach: Time O(N^2) Space O(1)

# Leetcode: https://leetcode.com/problems/palindromic-substrings/
# Solution:
def countSubstrings(s):
    def expand(left,right):
        count=0
        while left>=0 and right<len(s) and s[left]==s[right]:
            count+=1
            left-=1
            right+=1
        return count
    result=0
    for i in range(len(s)):
        result+=expand(i,i)      # Odd Length Palindrome
        result+=expand(i,i+1)    # Even Length Palindrome
    return result
# Test Cases
print(countSubstrings("abc"))  # Output: 3
print(countSubstrings("aaa"))  # Output: 6
