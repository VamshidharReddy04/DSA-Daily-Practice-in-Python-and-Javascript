# Array Problem: Three Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1: Input: nums = [-1,0,1,2,-1,-4] Output: [[-1,-1,2],[-1,0,1]]
# Example 2: Input: nums =[1,0,1] Output: []
# Example 3: Input: nums = [0,0,0] Output: [0,0,0]

# Solution: Two Pointer Approach

# Leetcode Link: https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums):
        nums.sort()  # Sort the array to use two-pointer technique
        result = []  # To store the result triplets
        n = len(nums)
        for i in range(n - 2):
            # Skip duplicate elements for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1  
            while left < right:
                threesum = nums[i] + nums[left] + nums[right]  # Sum of the triplet

                if threesum == 0:  # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]]) # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1                                     # Skip duplicates for the third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # Move both pointers after recording a valid triplet
                    left += 1
                    right -= 1
                elif threesum < 0:
                    left += 1  # Increase sum by moving left pointer right
                else:
                    right -= 1  # Decrease sum by moving right pointer left

        return result  # Return the list of triplets

# Test Cases
print(Solution().threeSum([-1,0,1,2,-1,-4]))  # Expected Output: [[-1,-1,2], [-1,0,1]]
print(Solution().threeSum([1,0,1]))  # Expected Output: []
print(Solution().threeSum([0,0,0]))  # Expected Output: [[0,0,0]]

# Best Approach : Optimized Two Pointer Approach
# Complexity Analysis: Time complexity: O(n^2) , Space complexity: O(1)