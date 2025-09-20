# Dynamic Programming : Decode Ways
# Given a string s containing only digits, return the number of ways to decode it.
# If the string is empty or starts with '0', return 0.
# Example 1: Input: s = "12" Output: 2
# Example 2: Input: s = "226" Output: 3
# Example 3: Input: s = "06" Output: 0

# Different Approaches:
# 1. Recursion (Brute Force) : Time Complexity O(2^n) | Space Complexity O(n)
# 2. Recursion + Memoization (Top-Down DP) : Time Complexity O(n) | Space Complexity O(n)
# 3. Dynamic Programming (Bottom-Up DP) : Time Complexity O(n) | Space Complexity O(n)
# 4. Space Optimization : Time Complexity O(n) | Space Complexity O(1)

# Solution 4: Space Optimization
#Leetcode : https://leetcode.com/problems/decode-ways/
class Solution :
    def decodeWays(self,s):
        n=len(s)                # n = length of the string
        if n ==0 or s[0] == "0": # If the string is empty or starts with '0', return 0
            return 0 
        dp =[0]*(n+1)  # Create a dp array of size n+1
        dp[n] =1          # Base case: An empty string has one way to decode
        dp[n-1] = 1 if s[n-1]!= '0' else 0 # If the last character is not '0', there's one way to decode it
        for i in range(n-2 ,-1,-1 ): #Second last index to 0 index
            if s[i]=='0': # If the current character is '0', there are no ways to decode it
                dp[i]=0
            else:
                dp[i] = dp[i+1]   # Single digit decode
                if 10 <= int(s[i:i+2]) <= 26: # Two digit decode
                    dp[i] += dp[i+2]  # Add the ways from two positions ahead
        return dp[0]          # Return the number of ways to decode the string
# Test Case
print(Solution().decodeWays("226")) # Output: 3
print(Solution().decodeWays("12")) # Output: 2
print(Solution().decodeWays("06")) # Output: 0

# Best Approach: Space Optimization
# Complexity Anaysis : Time O(n) | Space O(1)