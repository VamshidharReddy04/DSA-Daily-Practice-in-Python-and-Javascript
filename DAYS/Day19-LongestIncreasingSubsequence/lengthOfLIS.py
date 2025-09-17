# Dynamic Programming : Longest Increasing Subsequence (LIS)
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
# Example 1: Input: nums = [10,9,2,5,3,7,101,18]  Output: 4
# Example 2: Input: nums = [0,1,0,3,2,3]  Output: 4  
# Example 3: Input: nums = [7,7,7,7,7,7,7]  Output: 1  

# Different Approaches:
# 1. Recursion (Brute Force)
# 2. Memoization (Top-Down DP)
# 3. Tabulation (Bottom-Up DP)
# 4. Space Optimization (Optimized Bottom-Up DP)
# 5. Binary Search

# Solution 5: Binary Search (Patience Sorting)
import bisect
class Solution:
    def lengthOfLIS(self, nums ):
        sub=[]                  #sub array empty
        for num in nums:
            if not sub or num>sub[-1]:  #if sub is empty or num is greater than last element of sub
                sub.append(num)   #append num to sub
            else:
                idx=bisect.bisect_left(sub,num) #find the index of the first element in sub which is greater than or equal to num
                sub[idx]=num      #replace that element with num
        return len(sub)           #return the length of sub
# Test Cases:
print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))  # Output: 4
print(Solution().lengthOfLIS([0,1,0,3,2,3]))  # Output: 4
print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))  # Output: 1

# Best Approach : Binary Search (Patience Sorting)
# Complexity Analysis: Time Complexity: O(n log n) ,Space Complexity: O(n) (sub array)

# Solution 1: Recursion (Brute Force)
class BruteForceSolution:
    def lengthOfLIS(self, nums ):
        def helper(index, prev):
            if index == len(nums):
                return 0
            # Not take the current element
            not_take = helper(index + 1, prev)
            # Take the current element if it's greater than the previous one
            take = 0
            if nums[index] > prev:
                take = 1 + helper(index + 1, nums[index])
            return max(take, not_take)
        return helper(0, float('-inf'))
# Test Cases:
print(BruteForceSolution().lengthOfLIS([10,9,2,5,3,7,101,18]))  # Output: 4
print(BruteForceSolution().lengthOfLIS([0,1,0,3,2,3]))  # Output: 4
print(BruteForceSolution().lengthOfLIS([7,7,7,7,7,7,7]))  # Output: 1

# Complexity Analysis: Time Complexity: O(2^n) ,Space Complexity: O(n) (recursion stack)

# Solution 2: Memoization (Top-Down DP)
class MemoSolution:
    def lengthOfLIS(self, nums ):
        n = len(nums)
        dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
        def helper(index, prev_index): # helper function with index and previous index
            if index == n:
                return 0
            if dp[index][prev_index + 1] != -1:
                return dp[index][prev_index + 1]
            # Not take the current element
            not_take = helper(index + 1, prev_index)
            # Take the current element if it's greater than the previous one
            take = 0
            if prev_index == -1 or nums[index] > nums[prev_index]:
                take = 1 + helper(index + 1, index)
            dp[index][prev_index + 1] = max(take, not_take)
            return dp[index][prev_index + 1]
        
        return helper(0, -1)

# Test Cases:
print(MemoSolution().lengthOfLIS([10,9,2,5,3,7,101,18]))  # Output: 4
print(MemoSolution().lengthOfLIS([0,1,0,3,2,3]))  # Output: 4
print(MemoSolution().lengthOfLIS([7,7,7,7,7,7,7]))  # Output: 1
# Complexity Analysis: Time Complexity: O(n^2) ,Space Complexity: O(n^2) (dp array) + O(n) (recursion stack)

# Solution 3: Tabulation (Bottom-Up DP)
class TabulationSolution:
    def lengthOfLIS(self, nums ):
        n = len(nums)
        dp = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
# Test Cases:   
print(TabulationSolution().lengthOfLIS([10,9,2,5,3,7,101,18]))  # Output: 4
print(TabulationSolution().lengthOfLIS([0,1,0,3,2,3]))  # Output: 4
print(TabulationSolution().lengthOfLIS([7,7,7,7,7,7,7]))  # Output: 1
# Complexity Analysis: Time Complexity: O(n^2) ,Space Complexity: O(n) (dp array)

# Solution 4: Space Optimization (Optimized Bottom-Up DP)
class SpaceOptimizedSolution:
    def lengthOfLIS(self, nums ):
        n = len(nums)
        dp = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
# Test Cases:   
print(SpaceOptimizedSolution().lengthOfLIS([10,9,2,5,3,7,101,18]))  # Output: 4
print(SpaceOptimizedSolution().lengthOfLIS([0,1,0,3,2,3]))  # Output: 4
print(SpaceOptimizedSolution().lengthOfLIS([7,7,7,7,7,7,7]))  # Output: 1
# Complexity Analysis: Time Complexity: O(n^2) ,Space Complexity: O(n) (dp array)