# Array Problem: Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.


def maxSubArray(nums):
    # Initialize maxSum and curSum with the first element of nums
    maxSum =nums[0]
    curSum =0
    for num in nums:
        # Add the current element to curSum
        curSum += num
        # Update maxSum if curSum is greater
        maxSum = max(maxSum, curSum)
        # Reset curSum if it is negative
        if curSum < 0:
            curSum = 0
    return maxSum

# Test cases
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# Output: 6
print(maxSubArray([1]))
# Output: 1
print(maxSubArray([5,4,-1,7,8]))
# Output: 23

# Best Approach: Kadane's Algorithm
# complexity Analysis: time complexity: O(n), space complexity: O(1)