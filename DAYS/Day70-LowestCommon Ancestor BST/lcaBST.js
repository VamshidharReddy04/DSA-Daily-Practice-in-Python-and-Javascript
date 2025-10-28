// Binary Tree : Lowest Common Ancestor in a Binary Search Tree (LeetCode 235)
// Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
// Example 1: Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8 Output: 6
// Example 2: Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4 Output: 2
// Different Approaches:
// 1. Iterative BST Approach - Time O(h), Space O(1)
// 2. Recursive BST Approach - Time O(h), Space O(h)
// LeetCode Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
// Solution :
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}   

function lowestCommonAncestor(root, p, q) {
    while (root){
        if (p.val <root.val && q.val<root.val) root=root.left;
        else if(p.val>root.val && q.val>root.val) root=root.right;
        else return root;
    }
}
// Test Cases
let root1 = new TreeNode(6);
root1.left = new TreeNode(2);
root1.right = new TreeNode(8);
root1.left.left = new TreeNode(0);
root1.left.right = new TreeNode(4);
root1.left.right.left = new TreeNode(3);
root1.left.right.right = new TreeNode(5);
root1.right.left = new TreeNode(7);
root1.right.right = new TreeNode(9);
console.log(lowestCommonAncestor(root1, root1.left, root1.right).val); // Output: 6
console.log(lowestCommonAncestor(root1, root1.left, root1.left.right).val); // Output: 2


let root2 = new TreeNode(2);
root2.left = new TreeNode(1);
root2.right = new TreeNode(3);
console.log(lowestCommonAncestor(root2, root2, root2.left).val); // Output: 2

// Complexity Analysis: Time Complexity: O(h), Space Complexity: O(1)