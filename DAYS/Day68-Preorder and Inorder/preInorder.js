// Binary Tree Construction from Preorder and Inorder Traversal - (LeetCode 105)
// Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
// Example 1: Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] Output: [3,9,20,null,null,15,7]
// Example 2: Input: preorder = [-1], inorder = [-1] Output: [-1]
// Different Approaches:
// 1. Recursive Approach- Time O(N^2) Space O(N)
// 2. Optimized Recursive Approach using HashMap - Time O(N) Space O(N)

// LeetCode link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
// Solution:

function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
function buildTree(preorder, inorder) {
    let map=new Map();
    inorder.forEach((val, idx) => map.set(val, idx));
    let preIndex=0;
    function helper(left,right){
        if(left > right) return null;
        let rootVal=preorder[preIndex++];
        let root=new TreeNode(rootVal);
        let index=map.get(rootVal);
        root.left=helper(left, index-1);
        root.right=helper(index+1, right);
        return root;
    }
    return helper(0, inorder.length-1);
}
// Test Cases:
console.log(buildTree([3,9,20,15,7], [9,3,15,20,7]));
console.log(buildTree([-1], [-1]));

// Complexity Analysis: Time Complexity: O(N) Space Complexity: O(N)