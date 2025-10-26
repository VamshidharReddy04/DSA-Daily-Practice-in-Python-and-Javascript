# Binary tree- Maximum Depth (leetcode 104)
# Given the root of a binary tree, return its maximum depth.
# Example 1 : Input: root = [3,9,20,null,null,15,7] Output: 3
# Example 2 : Input: root = [1,null,2] Output: 2

# Different Approaches:
# 1. Recursive DFS- Time O(n), Space O(h)
# 2. Iterative BFS- Time O(n), Space O(w)

# Leetcode link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Solution :
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)

# Test cases
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(Solution().maxDepth(root))  # Output: 3

# Iterative BFS approach
from collections import deque
class SolutionBFS:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([root])
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return depth

# Both Approaches  Complexity Analysis: Time complexity O(n), Space complexity O(h) for DFS and O(w) for BFS