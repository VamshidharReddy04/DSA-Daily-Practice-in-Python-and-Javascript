# Binary Tree Level Order Traversal -LeetCode 102
# Given the root of a binary tree, return the level order traversal of its nodes' values
# Example 1: Input: root = [3,9,20,null,null,15,7] Output: [[3],[9,20],[15,7]]

# Different Approaches:
# 1. Iterative Approach using Queue (BFS) - Time O(N), Space O(N)
# 2. Recursive Approach (DFS) - Time O(N^2), Space O(N)

# Leetcode Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Solution :

from collections import deque
def levelOrder(root):
    if not root: return []
    res=[]
    queue=deque([root])
    while queue:
        level=[]
        for i in range(len(queue)):
            node=queue.popleft() # Dequeue the front node
            level.append(node.val) # Process the node
            if node.left: queue.append(node.left) # Enqueue left child  
            if node.right: queue.append(node.right) # Enqueue right child
        res.append(level) # Add current level to result
    return res
# Test Case
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Example Usage
if __name__ == "__main__":
    # Construct the binary tree [3,9,20,null,null,15,7]
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(2)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(levelOrder(root))  # Output: [[4], [9, 2], [15, 7]]

# Complexity Analysis: Time Complexity: O(N), Space Complexity: O(N)