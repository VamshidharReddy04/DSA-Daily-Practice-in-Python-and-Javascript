# Intervals - Non-overlapping Intervals
# Given an array of intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Example 1:Input: intervals = [[1,2],[2,3],[3,4],[1,3]] Output: 1
# Example 2:Input: intervals = [[1,2],[1,2],[1,2]] Output: 2
# Example 3:Input: intervals = [[1,2],[2,3]] Output: 0

# Different approach:
# 1.Brute Force - Time Complexity: O(n^2) Space Complexity: O(1)
# 2.Greedy - Time Complexity: O(n log n) Space Complexity: O(1)
# 3.Dynamic Programming - Time Complexity: O(n^2) Space Complexity: O(n)

# Solution 2: Greedy
# LeetCode: https://leetcode.com/problems/non-overlapping-intervals/description/
class Soultion:
    def nonOver(intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        count=0
        prev_end=intervals[0][1] # end of first interval
        for i in range(1,len(intervals)):
            if intervals[i][0]<prev_end:  # overlapping
                count +=1  # increment count
            else:
                prev_end=intervals[i][1] # update end to current interval's end
        return count    
# Test Cases:
print(Soultion.nonOver([[1,2],[2,3],[3,4],[1,3]])) # Output: 1
print(Soultion.nonOver([[1,2],[1,2],[1,2]])) # Output: 2
print(Soultion.nonOver([[1,2],[2,3]])) # Output: 0

# Best Approach: Greedy
# Complexity Analysis: Time Complexity: O(n log n) Space Complexity: O(1)