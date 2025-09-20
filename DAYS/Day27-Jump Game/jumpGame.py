# Greedy + Dynamic Programming : Jump Game
# Given an integer array nums, you are initially positioned at the array's first index.
# Example 1: Input: nums = [2,3,1,1,4] Output: true
# Example 2: Input: nums = [3,2,1,0,4] Output: false

# Different Approaches:
# 1. Greedy Approach - Time O(n) Space O(1)
# 2. Dynamic Programming - Time O(n) Space O(n)

# SOlution 1: Greedy Approach
# LeetCode Link: https://leetcode.com/problems/jump-game/solutions/2905016/python-greedy-solution-with-explanation/

class Solution:
    def canJump(nums):
        maxReach =0 # maximum reachable index
        for i in range(len(nums)):
            if i>maxReach:  # if current index is greater than maximum reachable index
                return False # we cannot reach this index
            maxReach =max(maxReach,i+nums[i]) # update maximum reachable index
        return True # if we can reach the last index
# Test Cases
print(Solution.canJump([2,3,1,1,4])) # True
print(Solution.canJump([3,2,1,0,4])) # False

# Best Approach: Greedy Approach
# Complxity Anaysis: Time O(n) Space O(1)