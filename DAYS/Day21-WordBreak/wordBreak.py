# Dynamic Programming: Word Break Problem
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Example 1: Input: s = "leetcode", wordDict = ["leet", "code"] Output: true Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2: Input: s = "applepenapple", wordDict = ["apple", "pen"] Output: true Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Example 3: Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"] Output: false

# Different Approaches:
# 1. Recursion (Brute Force)
# 2. Recursion with Memoization
# 3. Dynamic Programming


# Solution 3: Dynamic Programming
# Leetcode: https://leetcode.com/problems/word-break/
class Solution:
    def wordBreak(self,s,wordDict): 
        wordset=set(wordDict)  # Convert list to set for O(1) lookups
        n=len(s)               # Length of the string
        dp=[False]*(n+1)       # DP array to store results
        dp[0]=True          # Base case: empty string can be segmented
        for i in range(1,n+1):
            for j in range(i):  
                if dp[j] and s[j:i] in wordset: # Check if s[j:i] is in the dictionary
                    dp[i]=True                 # If it is, then s[0:i] can be segmented
                    break
        return dp[n]    # Return whether the entire string can be segmented
# Test Cases
print(Solution().wordBreak("leetcode", ["leet", "code"]))  # Output: True
print(Solution().wordBreak("applepenapple", ["apple", "pen"]))  # Output: True
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False

# Best Approach: Dynamic Programming
# Complexity Analysis: Time Complexity: O(n^2) Space Complexity: O(n)

# Approach 1: Recursion (Brute Force)
class Solution:
    def wordBreak(self,s,wordDict):   
        wordset=set(wordDict)  #
        n=len(s)               
        def dfs(i):            
            if i==0:          
                return True
            for j in range(i):
                if dfs(j) and s[j:i] in wordset:
                    return True   
            return False
        return dfs(n)    
# Test Cases
print(Solution().wordBreak("leetcode", ["leet", "code"]))  # Output
print(Solution().wordBreak("applepenapple", ["apple", "pen"]))  # Output: True
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False

# Complexity Analysis: Time Complexity: O(2^n) Space Complexity: O(n)

# Approach 2: Recursion with Memoization
class Solution:
    def wordBreak(self,s,wordDict):   
        wordset=set(wordDict)  
        n=len(s)             
        dp=[False]*(n+1)      
        def dfs(i):            
            if i==0:          
                return True
            if dp[i]:         
                return dp[i]
            for j in range(i):      
                if dfs(j) and s[j:i] in wordset:
                    dp[i]=True   
                    return True
            return False
        return dfs(n)          
# Test Cases
print(Solution().wordBreak("leetcode", ["leet", "code"]))  # Output: True
print(Solution().wordBreak("applepenapple", ["apple", "pen"]))  # Output: True
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False      

# Complexity Analysis: Time Complexity: O(n^2) Space Complexity: O(n)