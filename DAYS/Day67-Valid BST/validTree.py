# Binary Search Tree (BST) Validation -leetcode 98
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# Example 1: Input: root = [2,1,3] Output: true
# Example 2: Input: root = [5,1,4,null,null,3,6] Output: false

# Different Approaches:
# 1. Inorder Traversal: Time O(n), Space O(n)
# 2. Recursion with Range Limits: Time O(n), Space O(h)
# 
# Leetcode Link: https://leetcode.com/problems/validate-binary-search-tree/
# solution:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidTree(root):
        prev=[float('-inf')]
        def inorder(node):
            if not node:return True
            if not inorder(node.left):return False
            if node.val<=prev[0]:return False
            prev[0]=node.val
            return inorder(node.right)
        return inorder(root)
    
# Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    print(Solution.isValidTree(root1))  # Output: True

    # Example 2
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)
    print(Solution.isValidTree(root2))  # Output: False

# Complexity Analysis - Time complexity: O(n), Space complexity: O(h)
