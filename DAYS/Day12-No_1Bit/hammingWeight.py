# Binary Problem :No. of 1 Bits
# Write a function that takes an unsigned integer and returns the 
# number of '1' bits it has (also known as the Hamming weight).
# Example 1: Input: n = 11 Output: 3
# Example 2: Input: n = 128 Output: 1
# Example 3: Input: n = 2147483645  Output: 30

# Solution: Using Built-in Function
#LeetCode: https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n):
        count = 0  # Initialize count to 0
        while n:  # Loop until n becomes 0
            n = n & (n - 1)  # n & (n-1) will set the least significant bit to 0
            count += 1  # Increment count by 1
        return count  # Return the count of '1' bits
# Test Cases
print(Solution().hammingWeight(11)) #3
print(Solution().hammingWeight(128)) #1
print(Solution().hammingWeight(2147483645)) #30

# Best Approach: Brian Kernighan’s Algorithm
# Complexity Analysis: Time: O(1) Space: O(1)