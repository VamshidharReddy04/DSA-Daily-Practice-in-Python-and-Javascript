# Binary problem : Reverse Bits
# Given a 32-bit unsigned integer, reverse its bits and return the resulting integer.
# Example 1: Input: n = 00000010100101000001111010011100 Output: 964176192 (00111001011110000010100101000000)   
# Example 2: Input: n = 11111111111111111111111111111101 Output: 3221225471 (10111111111111111111111111111111)  

# LeetCode Link : https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self ,n):
        result =0
        for i in range(32):
            result =(result <<1) |(n&1)
            n >>=1
        return result
# Test cases

print(Solution().reverseBits(0b0000010100101000001111010011100)) # Output: 964176192
print(Solution().reverseBits(0b11111111111111111111111111111101)) # Output: 3221225471
print(Solution().reverseBits(43261596)) # Output: 964176192
print(Solution().reverseBits(4294967293)) # Output: 3221225471

# Complexity Analysis : Time complexity : O(1), Space complexity : O(1).