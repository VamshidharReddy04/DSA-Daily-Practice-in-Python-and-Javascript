// Binary Search Tree (BST) Validation -leetcode 98
// Given the root of a binary tree, determine if it is a valid binary search tree (BST).
// Example 1: Input: root = [2,1,3] Output: true
// Example 2: Input: root = [5,1,4,null,null,3,6] Output: false 
// Different Approaches: 
// 1. Inorder Traversal (Recursive) -Time: O(N), Space: O(N)
// 2. Recursive (DFS) -Time: O(N), Space: O(H)

// Leetcode Link: https://leetcode.com/problems/validate-binary-search-tree/
// Solution:

function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
function isValidBST(root) {
    let prev='infinity';
    function inorder(node){
        if(!node) return true;
        if(!inorder(node.left))return false;
        if(node.val<=prev)return false;
        prev=node.val;
        return inorder(node.right);
    }
    return inorder(root);
}
// Test Cases
let root1 = new TreeNode(2);
root1.left = new TreeNode(1);
root1.right = new TreeNode(3);
console.log(isValidBST(root1)); // true

let root2 = new TreeNode(5);
root2.left = new TreeNode(1);
root2.right = new TreeNode(4);
root2.right.left = new TreeNode(3);
root2.right.right = new TreeNode(6);
console.log(isValidBST(root2)); // false

// Complexity Analysis : Time Complexity: O(N) , Space Complexity: O(N)