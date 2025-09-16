# Binary Prproblem : Missing Number
# Given an array nums containing n distinct numbers in the range [0,..., n], 
# return the only number in the range that is missing from the array.
# Example 1: Input: nums = [3,0,1] Output: 2
# Example 2: Input: nums = [0,1] Output: 2
# Example 3: Input: nums = [9,6,4,2,3,5,7,0,1] Output: 8

# Solution 1: Using Gauss' Formula
# Solution 2: Using XOR

# Leetcode link: https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber (nums):
        # Solution 1: Using Gauss' Formula
        n=len(nums) 
        total=n*(n+1)//2  # Formula for sum of first n natural numbers
        sums=sum(nums)    # Sum of elements in the array
        return total-sums # The difference is the missing number
    
        # Solution 2: Using XOR
    def missingNumberXOR(nums):
        n=len(nums)  # Length of the array
        xorAll=0     # XOR of all numbers from 0 to n
        for i in range(n+1):  
            xorAll ^= i  # XOR of all numbers from 0 to n
        for num in nums:
            xorAll ^=num # XOR of all numbers in the array
        return xorAll

# Test Cases
print(Solution.missingNumber([3,0,1])) # Output: 2
print(Solution.missingNumber([0,1])) # Output: 2
print(Solution.missingNumber([9,6,4,2,3,5,7,0,1])) # Output: 8

print(Solution.missingNumberXOR([3,0,1])) # Output: 2
print(Solution.missingNumberXOR([0,1])) # Output: 2
print(Solution.missingNumberXOR([9,6,4,2,3,5,7,0,1])) # Output: 8                                                   

# Best Approach: 1. Using Gauss' Formula 2. Using XOR
# Complexity Analysis: Time Complexity: O(n) Space Complexity: O(1)
