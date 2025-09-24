# Linked List - Reverse a Linked List
# Type of Problem: Linked List manipulation,Pointer Reversal
# Given a singly linked list, reverse the list in-place and return the new head of the reversed list.
# Example 1:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
#  or Input: [1,2,3,4,5] Output: [5,4,3,2,1]
# Example 2: Input: 1 -> 2 -> NULL Output: 2 -> 1 -> NULL 
# Example 3: Input: NULL Output: NULL

# Different Approaches :
# 1. Iterative Approach: Use three pointers (prev, curr, next) - Time O(n), Space O(1)
# 2. Recursive Approach: Reverse the rest of the list and adjust pointers - Time O(n), Space O(n) due to recursion stack

# Solution Code (Iterative Approach):
# LeetCode Submission Link: https://leetcode.com/problems/reverse-linked-list/submissions/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, head):
        prev=None
        curr=head
        while curr: # Traverse the list
            next_node=curr.next # Store next node
            curr.next=prev # Reverse current node's pointer
            prev=curr     # Move pointers one position ahead
            curr=next_node   # Move to next node
        return prev
# Helper function to print linked list values
def print_list(head):
    values = []
    curr = head
    while curr:
        values.append(curr.val) 
        curr = curr.next
    print(values)

# Create test linked lists
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head2 = ListNode(1, ListNode(2))
head3 = None

solution = Solution()
print_list(solution.reverse(head1))  # Output: [5,4,3,2,1]
print_list(solution.reverse(head2))  # Output: [2,1]
print_list(solution.reverse(head3))  # Output: []

# Best Approach: Iterative Approach
# Complexity Analysis: 
# Time complexity: O(n) where n is the number of nodes in the linked list.
# Space complexity: O(1) as we are using only a constant amount of extra space.