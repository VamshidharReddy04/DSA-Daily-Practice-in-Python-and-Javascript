# Intervals - Meeting Room 1
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
#  determine if a person could attend all meetings.
# Example 1: Input: [[0,30],[5,10],[15,20]] Output: false
# Example 2: Input: [[7,10],[2,4]] Output: true
# Different Approaches:
# 1. Sorting and Comparing Adjacent Intervals (Greedy Approach) - Time O(n log n), Space O(1)
# 2. Using a Min-Heap (Priority Queue) - Time O(n log n), Space O(n)

# Solution 1: Sorting and Comparing Adjacent Intervals
# LeetCode: https://leetcode.com/problems/meeting-rooms/
class SOlution:
    def attendMeetings(intervals):
        # Sort the intervals based on start time
        intervals.sort(key=lambda x: x[0])
        # Compare each interval with the next one
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]: # Overlapping intervals
                return False
        return True
# Test Cases
print(SOlution.attendMeetings([[0,30],[5,10],[15,20]])) # Output: False
print(SOlution.attendMeetings([[7,10],[2,4]])) # Output: True

# Complexity Analysis: Time Complexity : O(nlogn) , Space Complexity : O(1)