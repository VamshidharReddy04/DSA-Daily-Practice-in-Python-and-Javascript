# Binary Tree : Lowest Common Ancestor in a Binary Search Tree (LeetCode 235)
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# Example 1: Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8 Output: 6
# Example 2: Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4 Output: 2
# Different Approaches: 
# 1. Iterative BST Approach-Time O(h), Space O(1)
# 2. Recursive BST Approach-Time O(h), Space O(h)

# Leetcode link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Solution:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val: root = root.left
            elif p.val > root.val and q.val > root.val: root = root.right
            else:return root
# Test Cases:
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
p = root.left # 2
q = root.right # 8
lca = Solution().lowestCommonAncestor(root, p, q)
print(lca.val) # Output: 6

root1 = TreeNode(6)
root1.left = TreeNode(2)
root1.right = TreeNode(8)
root1.left.left = TreeNode(0)
root1.left.right = TreeNode(4)
root1.left.right.left = TreeNode(3)
root1.left.right.right = TreeNode(5)
root1.right.left = TreeNode(7)
root1.right.right = TreeNode(9)
p1 = root1.left # 2
q1 = root1.left.right # 4
lca1 = Solution().lowestCommonAncestor(root1, p1, q1)
print(lca1.val) # Output: 2

# Additional test: tree [2,1,3], p=3, q=1
# Expected LCA (standard BST definition) is 2 (the root).
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
p2 = root2.right  # 3
q2 = root2.left   # 1
lca2 = Solution().lowestCommonAncestor(root2, p2, q2)
print(lca2.val)  # Output: 2

# Complexity Analysis: Time Complexity: O(h), Space Complexity: O(10