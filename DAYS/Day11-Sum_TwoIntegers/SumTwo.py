# Binary Problem - Sum Two Numbers
# Given two integers, return their sum without using the '+' and '-' operator.
# Example 1: input: a = 1, b = 2; output: 3
# Example 2: input: a = -2, b = 3; output:1
# Example 3: input: a = 2, b = 3; output: 5

# Approach: Bit Manipulation , using XOR and AND operations
# XOR operation gives sum without carry and AND operation gives carry bits.
# We repeat this process until there is no carry left.
# Leetcode: https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a, b):
        # 32 bits integer max and mask
        max = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b != 0:
            sum = (a ^ b) & mask  # sum without carry
            carry = ((a & b) << 1) & mask  # carry
            a, b = sum, carry
        # if a is negative, get a's two's complement positive value then return negative value
        return a if a <= max else ~(a ^ mask)
# Test cases
print(Solution().getSum(1,2)) # Output: 3
print(Solution().getSum(-2,3)) # Output: 1
print(Solution().getSum(2,3)) # Output: 5

# Best Approach: Bit Manipulation
# Complexity Analysis: Time Complexity: O(1), Space Complexity: O(1)