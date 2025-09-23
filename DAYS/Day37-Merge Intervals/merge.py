# Intervals - Merge Overlapping Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and 
# return an array of the non-overlapping intervals that cover all the intervals in the input.
# Example 1: Input: intervals = [[1,3],[2,6],[8,10],[15,18]] Output: [[1,6],[8,10],[15,18]]
# Example 2: Input: intervals = [[1,4],[4,5]] Output: [[1,5]]

# Different Approaches:
# 1. Sorting and Merging - Time Complexity: O(n log n) , Space Complexity: O(n)
# 2. Using a Stack - Time Complexity: O(n log n) , Space Complexity: O(n)
# 3. Using a Sweep Line Algorithm - Time Complexity: O(n log n) , Space Complexity: O(n)
# Solution 1 : Sorting and Merging
# LeetCode Link: https://leetcode.com/problems/merge-intervals/description/
class Solution:
    def merge(intervals):
        if not intervals: return []
        intervals.sort(key=lambda x:x[0])
        merged=[]
        for interval in intervals:
            if not merged or merged[-1][1]<interval[0]: # no overlap
                merged.append(interval) # add new interval
            else:
                merged[-1][1]=max(merged[-1][1],interval[1]) # merge intervals
        return merged # return merged intervals
# Test Cases
print(Solution.merge([[1,3],[2,6],[8,10],[15,18]])) # Output: [[1,6],[8,10],[15,18]]
print(Solution.merge([[1,4],[4,5]])) # Output: [[1,5]]

# Best Approach : Sorting and Merging
# Complexity Analysis: Time Complexity: O(n log n) , Space Complexity: O(n)