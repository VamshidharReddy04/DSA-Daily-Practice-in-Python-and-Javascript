# Binary Problem : Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Example 1: Input: nums = [2,2,1] Output: 1
# Example 2: Input: nums = [4,1,2,1,2] Output: 4
# Example 3: Input: nums = [1] Output: 1
# Solution : XOR

# Leetcode Link : https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self,nums):
        result = 0          # Initialize result to 0
        for num in nums:   # Iterate through each number in the array
            result ^= num   # Apply XOR operation    
        return result  # Return the single number
# Test Case
print(Solution().singleNumber([4,1,2,1,2])) # Output: 4
print(Solution().singleNumber([2,2,1])) # Output: 1
print(Solution().singleNumber([1])) # Output: 1

# Approach : XOR Operator
# Complexity Analysis : Time : O(N) , Space : O(1)