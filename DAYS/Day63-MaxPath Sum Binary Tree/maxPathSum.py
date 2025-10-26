# Binary Tree Maximum Path Sum- LeetCode 124
# Given a non-empty binary tree, find the maximum path sum.
# Example 1: Input: root = [1,2,3] Output: 6
# Example 2: Input: root = [-10,9,20,null,null,15,7] Output: 42
# Different Approaches: 
# 1. Recursive Depth-First Search (DFS) - Time O(n) , Space O(n)
# 2. Iterative Depth-First Search (DFS) with Stack - Time O(n) , Space O(n)
# Leetcode Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Solution :
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')
        def dfs(node):
            nonlocal max_sum
            if not node: return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            cur_path=node.val+left+right
            max_sum=max(max_sum,cur_path)
            return max(left,right)+node.val
        dfs(root)
        return max_sum
# Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(4)
    print(Solution().maxPathSum(root1))  # Output: 7

    # Example 2
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(10)
    root2.right.right = TreeNode(7)
    print(Solution().maxPathSum(root2))  # Output: 37

# Complexity Analysis -Time Complexity: O(n) , Space Complexity: O(n)