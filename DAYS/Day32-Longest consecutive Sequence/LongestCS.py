# Array+Hashset
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# Example 1: Input: nums = [100,4,200,1,3,2] Output: 4
# Example 2: Input: nums = [0,3,7,2,5,8,4,6,0,1] Output: 9
# Note: O(n) time and O(n) space
# Different Approaches:
# 1.Sorting: Time: O(n log n), Space: O(1) or O(n) depending on sorting algorithm
# 2.HashSet: Time: O(n), Space: O(n)

# Solution 2: HashSet
# LeetCode: https://leetcode.com/problems/longest-consecutive-sequence/solution/

class Solution:
    def longestConsecutive(self, nums):
        if not nums: return 0
        numSet=set(nums) 
        longest =0
        for n in numSet:  # Check only for the start of a sequence
            if n-1 not in numSet: # n is the start of a sequence
                length =1  # Current length of this sequence
                current=n  # Start of the sequence
                while current+1 in numSet: # Check for the next elements in the sequence
                    current+=1 # Move to the next element
                    length+=1 # Increment the length of the sequence
                longest=max(longest,length) # Update the longest length found
        return longest
# Test Cases
print(Solution().longestConsecutive([100,4,200,1,3,2])) # 4
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9

# Best Approach: HashSet
# Complexity Analysis: Time Complexity: O(n) Space Complexity: O(n)