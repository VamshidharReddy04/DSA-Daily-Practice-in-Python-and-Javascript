# Dynamic Programming : Longest Palindromic Substring (Leetcode 5)
# Given a string s, return the longest palindromic substring in s.
# Example 1: Input: s = "babad" Output: "bab" or "aba"
# Example 2: Input: s = "cbbd" Output: "bb"

# Different Approaches:
# 1. Brute Force -Time O(n^3), Space O(1)
# 2. Dynamic Programming - Time O(n^2), Space O(n^2)
# 3. Expand Around Center - Time O(n^2), Space O(1)
# 4. Manacher's Algorithm - Time O(n), Space O(n)

# Leetcode Link: https://leetcode.com/problems/longest-palindromic-substring/
# Solution:
class Solution:
    def longestPalindromeSubstring(s):
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        start=0
        maxLength=1
        for i in range(n):
            dp[i][i]=True
        for length in range(2,n+1):
            for i in range(n-length+1):
                j=i+length-1
                if s[i]==s[j]:
                    if length==2:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                    if dp[i][j] and length>maxLength:
                        start=i
                        maxLength=length
        return s[start:start+maxLength]
# Test Cases:
print(Solution.longestPalindromeSubstring("babad"))  # Output: "bab" or "aba"
print(Solution.longestPalindromeSubstring("cbbd"))   # Output: "bb"
# Best Approach: Manacher's Algorithm
# Complexity Analysis: Time complexity O(n), Space complexity O(n)
