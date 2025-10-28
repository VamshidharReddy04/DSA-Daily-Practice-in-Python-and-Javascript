# Binary Tree- Kth Smallest Element in a BST (Leetcode 230)
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
# Example 1: Input: root = [3,1,4,null,2], k = 1 Output: 1
# Example 2: Input: root = [5,3,6,2,4,null,null,1], k = 3 Output: 3
# Different Approaches:
# 1. Inorder Traversal (Recursive)- Time O(N), Space O(N)
# 2. Min-Heap- Time O(N log N), Space O(N)

# Leetcode link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    @staticmethod
    def kSmallest(root, k):
        stack = []  # Stack to store nodes
        curr = root
        while True:
            # go to leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left
            if not stack:
                # k is larger than number of nodes
                return None
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val                                                                                        
            # visit right subtree
            curr = node.right
# Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)
    k1 = 1
    print(Solution.kSmallest(root1, k1))  # Output: 1
    
    # Example 2
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)
    k2 = 3
    print(Solution.kSmallest(root2, k2))  # Output: 3

    # Edge case: k out of range
    print(Solution.kSmallest(root2, 10))  # Output: None

#  Complexity Analysis : Time Complexity: O(H), Space Complexity: O(H)