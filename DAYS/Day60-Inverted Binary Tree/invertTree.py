# Binary Tree- Inverted binary tree Leetcode 226
# Given the root of a binary tree, invert the tree, and return its root.
# Example 1: input: root = [4,2,7,1,3,6,9] output: [4,7,2,9,6,3,1]
# Example 2: input: root = [2,1,3] output: [2,3,1]

# Different Approaches:
# 1. Recursive DFS - Time: O(n), Space: O(n)
# 2. Iterative BFS(LOT) - Time: O(n), Space: O(n)
# Leetcode link: https://leetcode.com/problems/invert-binary-tree/
# Solution 1: Recursive DFS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        if not root: return None
        root.left,root.right=root.right,root.left  # swap left and right
        self.invertTree(root.left)  # invert left subtree
        self.invertTree(root.right)  # invert right subtree
        return root
# Test Cases
root1 = [4,2,7,1,3,6,9];
print(Solution().invertTree(root1))  # Output: [4,7,2,9,6,3,1]
root2 = [2,1,3];
print(Solution().invertTree(root2))  # Output: [2,3,1]

# Solution 2: Iterative BFS(LOT)
def invertTreeBFS(root):
    if not root: return None
    queue = [root]
    while queue:
        node = queue.pop(0)
        node.left, node.right = node.right, node.left  # swap left and right
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root
# Test Cases
root3 = [4,2,7,1,3,6,9];
print(invertTreeBFS(root3))  # Output: [4,7,2,9,6,3,1]
root4 = [2,1,3];
print(invertTreeBFS(root4))  # Output: [2,3,1]

# Best Approach: Both approaches have the same time and space complexity of O(n).