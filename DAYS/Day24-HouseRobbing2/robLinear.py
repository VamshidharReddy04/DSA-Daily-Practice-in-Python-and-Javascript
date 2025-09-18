# Dynamic Programming:Robber House Problem (Cricular)
# Given n houses in a circle, each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
# Robber has to rob all the houses with the maximum amount of money.

# Example 1: Input: nums = [2,3,2] Output: 3
# Example 2: Input: nums = [1,2,3,1] Output: 4
# Example 3: Input: nums = [0] Output: 0
# Different Approach:
# 1. Recursion (Brute Force)
# 2. Recursion + Memoization (Top Down)
# 3. Tabulation (Bottom Up)
# 4. Space Optimization
# 5. Circular House Robber

# Approach 4: Space Optimization
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        # Helper function for linear house robbing
        def rob_linear(arr):
            prev1, prev2 = 0, 0
            for num in arr:
                curr = max(num + prev2, prev1)
                prev2 = prev1
                prev1 = curr
            return prev1
        # Exclude first house or last house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))    
# Test Cases
print(Solution().rob([2,3,2])) # 3
print(Solution().rob([1,2,3,1])) # 4
print(Solution().rob([0])) # 0
# Best Approach : Space Optimization
# Complexity Analysis: Time O(n) | Space O(1)

class RobSolution:
    def rob(self, nums):
        def robing(nums):
            prev1, prev2 = 0, 0
            for num in nums:
                curr = max(num + prev2, prev1)
                prev2 = prev1
                prev1 = curr
            return prev1
        return max(robing(nums[:-1]), robing(nums[1:]))
print(RobSolution().rob([2,3,2])) # 3
print(RobSolution().rob([1,2,3,1])) # 4
print(RobSolution().rob([0])) # 0
# Complexity Analysis: Time O(n) | Space O(1)
    

# class CircularRobSolution:
#     def rob(self, nums):
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         return max(self.robRange(nums, 0, n - 2), self.robRange(nums, 1, n - 1))
#     def robRange(self, nums, start, end):
#         prev1 = 0
#         prev2 = 0
#         for i in range(start, end + 1):
#             take = nums[i] + prev2
#             notTake = 0 + prev1
#             curr = max(take, notTake)
#             prev2 = prev1
#             prev1 = curr
#         return prev1
# Test Cases
# print(CircularRobSolution().rob([2,3,2])) # 3
# print(CircularRobSolution().rob([1,2,3,1])) # 4
# print(CircularRobSolution().rob([0])) # 0
