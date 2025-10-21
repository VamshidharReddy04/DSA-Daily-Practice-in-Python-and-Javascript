# Strings : Minimum Window Substring (LeetCode 76)
# Given two strings s and t, return the minimum window substring of s such that every character
# in t (including duplicates) is included in the window. If there is no such substring, return "".
# Example 1: Input: s = "ADOBECODEBANC", t = "ABC" Output: "BANC"
# Example 2: Input: s = "a", t = "a" Output: "a"
# Example 3: Input: s = "a", t = "aa" Output: ""
# Different Approaches:
# 1. Brute Force - time O(n^3) space O(1)
# 2. Sliding Window - time O(n) space O(1)
# Solution 2: Sliding Window
# Leetcode Link: https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(s,t):
        if t=="":return ""
    @staticmethod
    def minWindow(s: str, t: str) -> str:
        if not t:
            return ""
        # frequency map for characters in t
        count = {}
        for ch in t:
            count[ch] = count.get(ch, 0) + 1
        window = {}
        l = 0
        have = 0
        need = len(count)
        res = [-1, -1]
        resLen = float("inf")
        # Expand window with right pointer r
        for r, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            if ch in count and window[ch] == count[ch]:
                have += 1
            # Try to contract from the left while we still have a valid window
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                # remove leftmost char from window
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        if resLen == float("inf"):
            return ""
        return s[res[0]: res[1] + 1]
# Test Cases
print(Solution.minWindow("ADOBECODEBANC","ABC")) # Output: "BANC"
print(Solution.minWindow("a","a")) # Output: "a"    
print(Solution.minWindow("aaabbaaabbbcc","abc")) # Output: "abbbc"

# Best Approach : Sliding Window
# Complexity Analysis: Time Complexity: O(n) , Space Complexity: O(1)

