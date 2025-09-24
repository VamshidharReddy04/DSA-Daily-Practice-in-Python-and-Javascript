# Linked List Cycle Detection
# Type of problem: Linked List, Two Pointers
# Given a linked list, determine if it has a cycle in it.
# To represent a cycle in the given linked list, we use an integer pos which represents the
# Example 1: Input: head = [3,2,0,-4], pos = 1, Output: true
# Example 2: Input: head = [1,2], pos = 0, Output: true
# Example 3: Input: head = [1], pos = -1, Output: false

# Different Approaches:
# 1. Hashmap /Set - Time Complexity: O(n), Space Complexity: O(n)
# 2. Two Pointers - Time Complexity: O(n), Space Complexity: O(1)
# 3. Floyd’s Cycle-Finding Algorithm - Time Complexity: O(n), Space Complexity: O(1)

# Solution using Two Pointers / Floyd’s Cycle-Finding Algorithm
# LeetCode: https://leetcode.com/problems/linked-list-cycle/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    @staticmethod
    def cycleList(head):
        if not head or not head.next:
            return False
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Helper function to create linked list with cycle
def LinkedCycle(values, pos):
    if not values:
        return None
    # Create nodes
    nodes = [ListNode(val) for val in values]
    # Link nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    # Create cycle if pos >= 0
    if pos >= 0 and pos < len(nodes):
        nodes[-1].next = nodes[pos]
    return nodes[0]

# Test Cases
head1 = LinkedCycle([3, 2, 0, -4], 1)
print(Solution.cycleList(head1))  # Expected output: True
head2 = LinkedCycle([1, 2], 0)
print(Solution.cycleList(head2))  # Expected output: True
head3 = LinkedCycle([1], -1)
print(Solution.cycleList(head3))  # Expected output: False

    