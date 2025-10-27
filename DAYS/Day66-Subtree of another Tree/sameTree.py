# Binary Tree : SubTree of Another Tree (LeetCode 572)
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# Example 1 : Input: root = [3,4,5,1,2], subRoot = [4,1,2] Output: true
# Example 2 : Input: root = [3,4,5,1,2,null, null,0], subRoot = [4,1,2] Output: false
# Different Approaches:
# Approach 1: Recursive Comparison-Time O(N*M), Space O(H)
# Approach 2: Tree Serialization-Time O(N+M), Space O(N+M)

# Leetcode link: https://leetcode.com/problems/subtree-of-another-tree/
# Solution:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubTree(self, root, subRoot):
        if not subRoot: return True
        if not root:return False
        if self.isSameTree(root,subRoot):
            return True
        return self.isSubTree(root.left,subRoot) or self.isSubTree(root.right,subRoot)

    def isSameTree(self,s,t):
        if not s and not t: return True
        if s and t and s.val==t.val:
            return self.isSameTree(s.left,t.left) and self.isSameTree(s.right,t.right)
        return False
    
# Test Cases
if __name__ == "__main__":
    # Example 1
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    sol = Solution()
    print(sol.isSubTree(root, subRoot))  # Output: True

    # Example 2
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(0)

    subRoot2 = TreeNode(4)
    subRoot2.left = TreeNode(1)
    subRoot2.right = TreeNode(2)

    print(sol.isSubTree(root2, subRoot2))  # Output: False

# Complexity Analysis : Time Complexity: O(N*M) , Space Complexity: O(H)