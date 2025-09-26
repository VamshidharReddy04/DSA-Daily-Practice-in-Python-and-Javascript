# Linked List- Remove nth Node From End of List( leetcode 19)
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Example 1: Input: head = [1,2,3,4,5], n = 2 Output: [1,2,3,5]
# Example 2: Input: head = [1], n = 1 Output: []
# Example 3: Input: head = [1,2], n = 1 Output: [1]
# Different Approaches:
# 1. Two Pass Algorithm- Time O(N) Space O(1)
# 2. One Pass Algorithm- Time O(N) Space O(1)

# Solution 1: Two Pass Algorithm
# Leetcode submission link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/3873780/python-3-two-pass-solution-with-explanation/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNode(head, n):
        dummy=ListNode(0,head)
        fast=slow=dummy
        for i in range(n+1):
            fast=fast.next # Move fast pointer n+1 steps ahead
        while fast:
            slow=slow.next # Move both pointers until fast reaches the end
            fast=fast.next # Move fast pointer
        # Skip the nth node from the end
        slow.next=slow.next.next
        return dummy.next
# Helper function to create a linked list from a list
def printList(head):
    vals=[]
    while head:
        vals.append(head.val)
        head=head.next
    print(vals)
# Test Cases
head1=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
n1=2
printList(Solution.removeNode(head1,n1))  # Output: [1, 2, 3, 5]
head2=ListNode(1)
n2=1
printList(Solution.removeNode(head2,n2))  # Output: []
head3=ListNode(1,ListNode(2))
n3=1
printList(Solution.removeNode(head3,n3))  # Output: [1]

# Best Approach: One Pass Algorithm
# Complxity Analysis: Time O(N) Space O(1)