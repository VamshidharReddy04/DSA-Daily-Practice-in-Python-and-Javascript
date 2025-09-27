# Linked List - Reorder List (Leetcode problem 143)
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# You may not modify the values in the list's nodes, only nodes itself may be changed
# Example 1: Input: 1->2->3->4 Output: 1->4->2->3 
# Example 2: Input: 1->2->3->4->5 Output: 1->5->2->4->3 
# Different Approaches:
# 1. Brute Force/ Extra Data Structure - Time Complexity: O(n), Space Complexity: O(n)
# 2. Optimal Approach - Time Complexity: O(n), Space Complexity: O(1)

# Solution 2: Optimal Approach
# LeetCode Link: https://leetcode.com/problems/reorder-list/solution/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return head
        # Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next            # Move slow by 1 step
            fast = fast.next.next       # Move fast by 2 steps
        # Split the list into two halves
        second_half = slow.next     # Start of second half
        slow.next = None        # Terminate first half
        # Reverse Second half
        prev, curr = None, second_half
        while curr:      # Standard reverse linked list
            next = curr.next    # Store next node
            curr.next = prev    # Reverse the link
            prev = curr       # Move prev and curr one step forward
            curr = next   # Move curr one step forward
        # Merge two halves
        first, second = head, prev
        while second:       # Standard merge
            temp1 ,temp2= first.next,second.next
            first.next = second     # Link first to second
            second.next = temp1     # Link second to next of first
            first = temp1           # Update first and second
            second = temp2
        return head
# Helper function Printlist
def printList(head):
    val=[]
    while head:
        val.append(head.val)
        head=head.next
    print(val)
# Test Cases
list1=ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
head= Solution().reorderList(list1)
printList(head) # Output: [1, 4, 2, 3]
list2=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
head= Solution().reorderList(list2)
printList(head) # Output: [1, 5, 2, 4, 3]
list3=ListNode(1)
head= Solution().reorderList(list3)
printList(head) # Output: [1]

# Best Approach: Optimal Approach
# Complxity Analysis:Time Complexity: O(n), Space Complexity: O(1)

# Or Build linked list from array and test cases more than 5 nodes

# Build the linked list from array
def buildList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
# Test Case
head = buildList([1,2,3,4,5,6,7,8,9,10])
printList(Solution().reorderList(head)) # Output: 1->10->2->9->3->8->4->7->5->6