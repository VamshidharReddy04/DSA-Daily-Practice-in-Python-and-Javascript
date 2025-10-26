# Binary Tree Serialization and Deserialization - LeetCode 297
# Given the root of a binary tree, implement two functions:
# Example 1: Input: root = [1,2,3,null,null,4,5] Output: [1,2,3,null,null,4,5]
# Example 2: Input: root = [] Output: []

# Different approaches:
# 1. Preorder Traversal (DFS)- Time: O(n), Space: O(n)
# 2. Level Order Traversal with Queue (BFS)- Time: O(n), Space: O(n)
# LeetCode Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Solution:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Codec:
    def serialize(root):
        def dfs(node):
            if not node:
                vals.append('null')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        vals=[]
        dfs(root)
        return ','.join(vals)
    def deserialize(data):
        if not data:return None 
        vals=data.split(',')
        def build():
            if not vals: return None
            val= vals.pop(0)
            if val=='null': return None
            node=TreeNode(int(val))
            node.left=build()
            node.right=build()
            return node
        return build()
# Test Cases
if __name__ == "__main__":
    codec = Codec()
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(5)
    serialized1 = codec.serialize(root1)
    print("Serialized:", serialized1)
    deserialized1 = codec.deserialize(serialized1)
    print("Deserialized Root Value:", deserialized1.val)  # Should print 1

# Complexity Analysis: Time complexity O(n), Space complexity O(n)