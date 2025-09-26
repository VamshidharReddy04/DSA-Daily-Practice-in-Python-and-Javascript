# Linked List- Merge Two Sorted Lists (LeetCode Problem 21)
# Given the heads of two sorted linked lists list1 and list2, merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# Example 1: Input: list1 = [1,2,4], list2 = [1,3,4] Output: [1,1,2,3,4,4]
# Example 2: Input: list1 = [], list2 = [] Output: []
# Example 3: Input: list1 = [], list2 = [0] Output: [0]

# Difference Approach:
# 1. Iterative Approach (Using Dummy Nodes) -Time O(n+m) Space O(1)
# 2. Recursive Approach ( Recursion + Merging)- Time O(n+m) Space O(n+m) 
# Solution 1: Iterative Approach (Using Dummy Nodes)
# Leetcode Link: https://leetcode.com/problems/merge-two-sorted-lists/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def mergeList(list1,list2):
        dummy = ListNode(-1) # Dummy node to simplify edge cases
        tail=dummy # Tail pointer to build the merged list
        while list1 and list2:
            if list1.val<list2.val:
                tail.next=list1 # Append list1 node to merged list
                list1=list1.next # Move to next node in list1
            else:
                tail.next=list2 # Append list2 node to merged list
                list2=list2.next # Move to next node in list2
            tail=tail.next # Move tail to the last node
        # Append any remaining nodes from either list
        tail.next=list1 if list1 else list2
        return dummy.next # Return the merged list (skip dummy node)
# Helper function to print linked list
def printList(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)
# Test case 1: [1,2,4] and [1,3,4]
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
merged = Solution.mergeList(list1, list2)
printList(merged)  # Output: [1, 1, 2, 3, 4, 4]

# Test case 2: [] and []
list1 = None
list2 = None
merged = Solution.mergeList(list1, list2)
printList(merged)  # Output: []

# Test case 3: [] and [0]
list1 = None
list2 = ListNode(0)
merged = Solution.mergeList(list1, list2)
printList(merged)  # Output: [0]


