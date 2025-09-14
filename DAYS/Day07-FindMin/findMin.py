# Array Problem : Find Minimum in Rotated Sorted Array
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# Ex: [4,5,6,7,0,1,2] might become [0,1,2,4,5,6,7]
# Example 1: input: nums = [3,4,5,1,2] output: 1
# Example 2: input: nums = [4,5,6,7,0,1,2] output: 0
# Example 3: input: nums = [11,13,15,17] output: 11
# solution by Binary Search

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # If the middle element is greater than the rightmost element,
            # the minimum element must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # If the middle element is less than or equal to the rightmost element,
            # the minimum element must be in the left half.
            else:
                right = mid
        return nums[left]

# Test Cases
print(Solution().findMin([3,4,5,1,2]))  # Output: 1
print(Solution().findMin([4,5,6,7,0,1,2]))  # Output: 0
print(Solution().findMin([11,13,15,17]))  # Output: 11

# Best Approach: Binary Search
# Complexity Analysis: Time: O(log n) | Space: O(1)
