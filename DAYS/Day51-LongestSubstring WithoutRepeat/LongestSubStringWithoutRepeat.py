# Strings: Longest Substring Without Repeating Characters leetcode 3
# Given a string s, find the length of the longest substring without repeating characters.
# Example 1: Input: s = "abcabcbb" Output: 3
# Example 2: Input: s = "bbbbb" Output: 1
# Example 3: Input: s = "pwwkew" Output: 3

# Different Approaches:
# 1. Brute Force Approach: Time O(n^3) Space O(1)
# 2. Sliding Window Approach: Time O(2n) Space O(min(m,n))
# Solution 2: Sliding Window Approach
# Leetcode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/3030126/sliding-window-approach-python-java-c/

class Solution:
    @staticmethod
    def LongestSubString(s):
        left=maxLength=0
        seen={} # Last seen index of character
        for right in range(len(s)):
            if s[right] in seen:
                # Only move left forward; do not move it backward when seen[s[right]] < left
                left = max(left, seen[s[right]] + 1) # Move left pointer to the right of last seen index if needed
            seen[s[right]] = right # Update last seen index of character
            maxLength = max(maxLength, right - left + 1) # Update max length
        return maxLength
# Test Cases
print(Solution.LongestSubString("abcabcbb")) # Output: 3
print(Solution.LongestSubString("bbbbb")) # Output: 1   
print(Solution.LongestSubString("pwwkew")) # Output: 3
print(Solution.LongestSubString("abba")) # Output: 2

# Best Approach: Sliding Window Approach
# Complexity Analysis: Time complexity: O(n) Space complexity: O(n) 