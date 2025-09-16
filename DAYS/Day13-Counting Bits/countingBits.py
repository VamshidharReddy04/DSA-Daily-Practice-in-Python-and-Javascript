# Binary Problem - Counting Bits
# Given a non-negative integer num, for every number i in the range 0 ≤ i ≤ num,
# calculate the number of 1's in their binary representation and return them as an array.]
# Example 1: Input: 2 Output: [0,1,1]
# Example 2: Input: 5 Output: [0,1,1,2,1,2]

# Solution 1: Optimized Dynamic Programming
#LeetCode Link: https://leetcode.com/problems/counting-bits/description/

class Solution:
    def countingBits(self,n): 
        dp=[0]*(n+1)  # Initialize dp array
        for i in range(1,n+1):  
            dp[i]=dp[i>>1]+(i&1)  
        return dp 
# Test Case:
print(Solution().countingBits(5))  # Output: [0,1,1,2,1,2]
print(Solution().countingBits(2))  # Output: [0,1,1]

# Best Approach: Optimized Dynamic Programming
# Complexity Analysis: Time: O(n), Space: O(1)
