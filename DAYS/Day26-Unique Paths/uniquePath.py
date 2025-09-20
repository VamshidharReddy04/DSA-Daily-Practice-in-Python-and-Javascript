# Dynamic Programming: Unique Paths
# Problem: Given an integer m and n, return the number of possible unique paths that the robot 
# can take to reach the bottom-right corner of an m x n grid from the top-left corner.

# Example 1: Input: m = 3, n = 2 Output: 3
# Example 2: Input: m = 1, n = 3 Output: 1
# Different Approaches :
# 1. Recursion (Brute Force) - Time O(2^(m+n)) Space O(m+n)
# 2. Memoization (Top Down DP) - Time O(m*n) Space O(m*n)
# 3. Tabulation (Bottom Up DP) - Time O(m*n) Space O(m*n)
# 4. Space Optimization - Time O(m*n) Space O(n)

# Solution 4: Space Optimization
# Leetcode: https://leetcode.com/problems/unique-paths/description/

class Solution:
    def uniquePaths(self,m,n):
        dp=[1]*n # Initialize a 1D array with 1s
        for i in range(1,m):
            for j in range(1,n):
                dp[j]=dp[j]+dp[j-1] # Update the current cell with the sum of the top and left cells
        return dp[-1] # Return the last cell which contains the number of unique paths
# Test Case
print(Solution().uniquePaths(3,2)) # Output: 3
print(Solution().uniquePaths(1,3)) # Output: 1

# Best Approach: Space Optimization
# Complexity Analysis: Time O(m*n) Space O(n)