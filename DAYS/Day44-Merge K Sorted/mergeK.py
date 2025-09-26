# Linked List - Merge k Sorted Lists (Leetcode Problem #23)
# Given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Example 1: Input: lists = [[1,4,5],[1,3,4],[2,6]] Output: [1,1,2,3,4,4,5,6]
# Example 2: Input: lists = [] Output: []
# Example 3: Input: lists = [[]] Output: []
# Differnt Approaches:
# 1. Brute Force: Time O(N log N), Space O(N)
# 2. Sequential Merge: Time O(Nk), Space O(1)
# 3. Min Heap(Priority Queue): Time O(N log k), Space O(k)
# 4. Merge with Divide and Conquer: Time O(N log k), Space O(1)
# Solution 3: Min Heap/Priority Queue
# Leetcode Link: https://leetcode.com/problems/merge-k-sorted-lists/

import heapq
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    def mergeKSorted(self, lists):
        minHeap = []  # Min Heap to store the nodes
        dummy = ListNode(-1)  # Dummy node to help in merging
        tail = dummy  # Tail pointer to build the merged list
        for idx, node in enumerate(lists):
            if node:  # If the node is not None
                heapq.heappush(minHeap, (node.val, idx, node))  # Push the value, index and node to the heap
        # Process nodes from heap
        while minHeap:  # While the heap is not empty
            val, idx, node = heapq.heappop(minHeap)  # Pop the smallest node
            tail.next = node  # Append the node to the merged list
            tail = tail.next  # Move the tail pointer
            if node.next:  # If the node has a next node
                heapq.heappush(minHeap, (node.next.val, idx, node.next))  # Push the next node to the heap
        return dummy.next  # Return the merged list starting from the next of dummy node
    
# Helper function to print linked list
def printListNode(head):
    val=[]
    while head:
        val.append(head.val)
        head = head.next
    print(val)

# Test Cases
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
lists = [list1, list2, list3]
printListNode(Solution().mergeKSorted(lists))
printListNode(Solution().mergeKSorted([]))
printListNode(Solution().mergeKSorted([[]]))
