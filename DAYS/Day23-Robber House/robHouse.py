# Dynamic Programming: Rob the House
# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.
# Example 1: Input: nums = [1,2,3,1] Output: 4
# Example 2: Input: nums = [2,7,9,3,1] Output: 12
# Different Approaches: 
# 1.Recursion (Brute Force)
# 2.Memoization (Top-Down DP)
# 3.Tabulation (Bottom-Up DP)
# 4.Space Optimization

# Solution 4: Space Optimization
# LeetCode: https://leetcode.com/problems/house-robber/solutions/2924103/python-3-space-optimization-dp-solution-with-explanation/
class Solution:
    def rob(self,nums): 
        rob1,rob2=0,0   # Initialize two variables to store the maximum amount that can be robbed
        for n in nums:
            temp=max(n+rob1,rob2) # Maximum amount that can be robbed at the current house
            rob1=rob2 # Previous maximum amount that can be robbed
            rob2=temp # Current maximum amount that can be robbed
        return rob2 # Maximum amount that can be robbed
# Test Cases
print(Solution().rob([1,2,3,1])) # 4
print(Solution().rob([2,7,9,3,1])) # 12

# Best Approach: Space Optimization
# Complexity Analysis: Time Complexity: O(N) , Space Complexity: O(1)