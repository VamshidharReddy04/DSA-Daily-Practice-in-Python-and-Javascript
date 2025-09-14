# Array Problems - Search Target
# Given a sorted array of integers nums and an integer target,  return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and  you may not use the same element twice
# Example 1: Input: nums = [4,5,6,7,0,1,2], target = 0 Output: 4
# Example 2: Input: nums = [4,5,6,7,0,1,2], target = 3 Output: -1
# Example 3: Input: nums = [1], target = 0 Output: -1

# Solution Binary Search
# leetcode link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    @staticmethod
    def search(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            if nums[mid] == target:
                # If the middle element is the target, return the index
                return mid
            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if the target is in the left half
                if nums[left] <= target < nums[mid]:
                    # If the target is in the left half, update the right pointer
                    right = mid - 1
                else:
                    # If the target is not in the left half, update the left pointer
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    # If the target is in the right half, update the left pointer
                    left = mid + 1
                else:
                    right = mid - 1
        # If the target is not found, return -1
        return -1

# Test Cases
print(Solution.search([4,5,6,7,0,1,2], 0))  # Output: 4
print(Solution.search([4,5,6,7,0,1,2], 3))  # Output: -1
print(Solution.search([1], 0))  # Output: -1

# Best Approach: Binary Search
# Complexity Analysis: Time Complexity: O(log n) Space Complexity: O(1)
