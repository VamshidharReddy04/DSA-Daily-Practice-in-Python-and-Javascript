# Binary Tree Construction from Preorder and Inorder Traversal - (LeetCode 105)
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
# Example 1: Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] Output: [3,9,20,null,null,15,7]
# Example 2: Input: preorder = [-1], inorder = [-1] Output: [-1]
# Different Approaches: 
# 1. Recursive Approach - Time O(N), Space O(N)
# 2. Iterative Approach - Time O(N), Space O(N)
# Solution:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(preorder, inorder):
        if not preorder or not inorder:return None
        rootVal = preorder[0]
        root=TreeNode(rootVal)
        mid=inorder.index(rootVal)
        root.left=Solution.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=Solution.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root

# Test Cases
# Example 1
preorder1 = [3,9,20,15,7]
inorder1 = [9,3,15,20,7]
tree1 = Solution.buildTree(preorder1, inorder1)
print(tree1.val)  # Output: 3

# Example 2
preorder2 = [-1]
inorder2 = [-1]
tree2 = Solution.buildTree(preorder2, inorder2)
print(tree2.val)  # Output: -1

# Complexity Analysis: Time Complexity: O(N), Space Complexity: O(N)