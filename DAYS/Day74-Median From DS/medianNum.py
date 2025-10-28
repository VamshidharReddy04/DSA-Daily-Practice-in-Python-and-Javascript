# Heap : Median of a Data Stream (LeetCode 295)
# Given a stream of integers, implement a data structure that supports the following two operations:
# 1. void addNum(int num) - Add a integer number from the data stream
# 2. double findMedian() - Return the median of all elements in the data stream
# Example 1: Input: ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"] [[],[1],[2],[],[3],[]] Output: [null,null,null,1.5,null,2.0]

# Different Approaches:
# 1. Using Two Heaps (Min-Heap and Max-Heap)-Time O(log n) addNum, O(1) findMedian | Space O(n)
# 2. Using Sorted List - Time O(n) addNum, O(1) findMedian | Space O(n)

# Leetcode Link: https://leetcode.com/problems/median-of-a-data-stream/
# Solution:
import heapq
class MedianFinder:
    def __init__(self):
        self.large = []  # Min-heap for the larger half
        self.small = []  # Max-heap for the smaller half

    def addNum(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large,-heapq.heappop(self.small))
        if len(self.small)<len(self.large):
            heapq.heappush(self.small,-heapq.heappop(self.large))
    def findMedian(self):
        if len(self.small)>len(self.large):
            return -self.small[0]
        return (-self.small[0]+self.large[0])/2
# Test Cases
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(3)
print(medianFinder.findMedian())  # Output: 2.0
medianFinder.addNum(5)
print(medianFinder.findMedian())  # Output: 3.0

# Complexity Analysis: Time Complexity: O(log n) for addNum, O(1) for findMedian
# Space Complexity: O(n) for storing the numbers in heaps