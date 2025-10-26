# Binary tree - Same Tree (LeetCode 100)
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
# Example 1:Input: p = [1,2,3], q = [1,2,3] Output: true
# Example 2:Input: p = [1,2], q = [1,null,2] Output: false
# Different Approaches: 
# 1. Recursive DFS-Time O(n), Space O(n)
# 2. Iterative BFS-Time O(n), Space O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sameTree(p,q):
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return Solution.sameTree(p.left, q.left) and Solution.sameTree(p.right, q.right)

# Test Cases
if __name__ == "__main__":
    # Example 1
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)
    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)
    print(Solution.sameTree(p1, q1))  # Output: True

    # Example 2
    p2 = TreeNode(1)
    p2.left = TreeNode(2)
    q2 = TreeNode(1)
    q2.right = TreeNode(2)
    print(Solution.sameTree(p2, q2))  # Output: False
# Complexity Analysis:
# Time Complexity: O(n)
# Space Complexity: O(n)