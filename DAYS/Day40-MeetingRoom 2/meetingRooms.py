# Intervals : Meeting Rooms II
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required. 
# Example 1: Input: [[0, 30],[5, 10],[15, 20]] Output: 2
# Example 2: Input: [[7,10],[2,4]] Output: 1\

# Different Approaches:
# 1. Using Min-Heap (Priority Queue) - Time Complexity: O(N log N) Space Complexity: O(N)
# 2. Using Sorting - Time Complexity: O(N log N) Space Complexity: O(N)\

# Solution 1: Using Min-Heap (Priority Queue)
# Leetcode Link: https://leetcode.com/problems/meeting-rooms-ii/
import heapq
class Solution:
    def MeetRooms(intervals):
        if not intervals: 
            return 0
        intervals.sort(key=lambda x: x[0]) # Sort by start time
        heap=[] # Min-Heap to track end times of meetings
        for interval in intervals:
            if heap and heap[0]<=interval[0]: # If the room is free 
                heapq.heappop(heap) # Remove the room from heap
            heapq.heappush(heap,interval[1]) # Add the new meeting end time
        return len(heap)
# Test Case
print(Solution.MeetRooms([[0, 30],[5, 10],[15, 20]])) # Output: 2
print(Solution.MeetRooms([[7,10],[2,4]])) # Output: 1
# Best Approach: Min-Heap (Priority Queue) 
# Complexity Analysis: Time Complexity: O(N log N) Space Complexity: O(N)