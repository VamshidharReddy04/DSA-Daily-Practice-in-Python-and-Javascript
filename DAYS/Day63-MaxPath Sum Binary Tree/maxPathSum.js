// Binary Tree Maximum Path Sum- LeetCode 124
// Given a non-empty binary tree, find the maximum path sum.
// Example 1: Input: root = [1,2,3] Output: 6
// Example 2: Input: root = [-10,9,20,null,null,15,7] Output: 42
// Different Approach: 
// 1. Recursive DFS - Time O(n) , Space O(n)
// 2. Iterative DFS - Time O(n) , Space O(n)
//Leetcode Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
// Solution:
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
function maxPathSum(root){
    let maxsum=-Infinity;
    function dfs(node){
        if(!node) return 0;
        let left=Math.max(dfs(node.left),0);
        let right=Math.max(dfs(node.right),0);
        let currpath=node.val+left+right;
        maxsum=Math.max(maxsum,currpath);
        return node.val+Math.max(left,right);
    }
    dfs(root);
    return maxsum;
}
// Test Cases
if (require.main === module) {
    // Example 1
    let root1 = new TreeNode(1);
    root1.left = new TreeNode(2);
    root1.right = new TreeNode(4);
    console.log(maxPathSum(root1));  // Output: 7

    // Example 2
    let root2 = new TreeNode(-10);
    root2.left = new TreeNode(9);
    root2.right = new TreeNode(20);
    root2.right.left = new TreeNode(10);
    root2.right.right = new TreeNode(7);
    console.log(maxPathSum(root2));  // Output: 37
}
// Complexity Analysis -Time Complexity: O(n) , Space Complexity: O(n)