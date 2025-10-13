# Strings : Longest Repeating character Replacement leetcode 424
# Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.
# Example 1: Input: s = "ABAB", k = 2 Output: 4
# Example 2: Input: s = "AABABBA", k = 1 Output: 4
# Example 3: Input: s = "AAAA", k = 2 Output: 4


# Different Approaches: 
# 1. Brute Force -Time O(N^2) Space O(1)
# 2. Sliding Window - Time O(N) Space O(1)
# Solution 2: Sliding Window
# Leetcode: https://leetcode.com/problems/longest-repeating-character-replacement/discuss/100860/Python-Sliding-Window
class Solution:
    def characterReplacement(s,k):
        left,maxLength=0,0
        count={}
        for right in range(len(s)):
            char=s[right]
            count[char]=count.get(char,0)+1
            maxCount=max(count.values())
            while (right-left+1)-maxCount>k:
                count[s[left]]-=1
                left+=1
            maxLength=max(maxLength,right-left+1)
        return maxLength
# Test Cases
print(Solution.characterReplacement("ABAB",2)) #4
print(Solution.characterReplacement("AABABBA",2)) #5 (correct expected output for k=2)
print(Solution.characterReplacement("AAAA",2)) #4

# Best Approach: Sliding Window
# Complexity Analysis: Time complexity: O(N) , Space complexity: O(1)