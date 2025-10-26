// Binary Tree- Same Tree (LeetCode 100)
// Given the roots of two binary trees p and q, write a function to check if they are the same or not.
// Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
// Example 1: Input: p = [1,2,3], q = [1,2,3] Output: true
// Example 2: Input: p = [1,2], q = [1,null,2] Output: false
// Example 3: Input: p = [1,2,1], q = [1,1,2] Output: false

// Different Approaches:
// 1. Recursive Approach - Time O(n), Space O(n)
// 2. Iterative Approach using BFS - Time O(n), Space O(n)

// Leetcode link: https://leetcode.com/problems/same-tree/
// Solution:
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
function sameTree(p,q){
    if(!p && !q) return true;
    if(!p || !q || p.val !== q.val) return false;
    return sameTree(p.left, q.left) && sameTree(p.right, q.right);
}
// Test Cases
const tree1 = new TreeNode(1, new TreeNode(2), new TreeNode(3));
const tree2 = new TreeNode(1, new TreeNode(2), new TreeNode(3));
console.log(sameTree(tree1, tree2)); // true
const tree3 = new TreeNode(1, new TreeNode(2), null);
const tree4 = new TreeNode(1, null, new TreeNode(2));
console.log(sameTree(tree3, tree4)); // false
const tree5 = new TreeNode(1, new TreeNode(2), new TreeNode(1));
const tree6 = new TreeNode(1, new TreeNode(1), new TreeNode(2));
console.log(sameTree(tree5, tree6)); // false

// Both Approches Complexity Analysis:Time Complexity: O(n) , Space Complexity: O(n)