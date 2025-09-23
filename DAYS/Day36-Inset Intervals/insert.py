# Intervals- Insert Interval
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# Example 1: Input: intervals = [[1,3],[6,9]], newInterval = [2,5] Output: [[1,5],[6,9]]
# Example 2: Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8] Output: [[1,2],[3,10],[12,16]]
# Differnt Approaches:
# 1. Brute Force: O(n) time, O(n) space
# 2. Optimal Approach: O(n) time, O(1) space

# Solution 2: Optimal Approach
# LeetCode: https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(intervals,newInterval):
        res=[]
        for i in intervals:
            if i[1]<newInterval[0]: # No overlap, interval before newInterval
                res.append(i) # Add the interval to result
            elif i[0]>newInterval[1]: # No overlap, interval after newInterval
                res.append(newInterval) # Add newInterval to result
                newInterval=i # Update newInterval to current interval
            else:
                newInterval[0]=min(newInterval[0],i[0]) # Overlap, merge intervals
                newInterval[1]=max(newInterval[1],i[1]) # Update the end of newInterval
        res.append(newInterval) # Add the last newInterval
        return res
# Test Cases
print(Solution.insert([[1,3],[6,9]],[2,5])) # Output: [[1,5],[6,9]]
print(Solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])) # Output: [[1,2],[3,10],[12,16]]

# Best Solution: Optimal Approach
# Complexity Analysis: Time: O(n), Space: O(1)