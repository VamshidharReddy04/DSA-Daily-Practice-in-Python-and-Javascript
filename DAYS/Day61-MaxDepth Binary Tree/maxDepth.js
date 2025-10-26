// Maximum Depth of Binary Tree - LeetCode 104
// Given the root of a binary tree, return its maximum depth.
// Example 1: Input: root = [3,9,20,null,null,15,7] Output: 3
// Example 2: Input: root = [1,null,2] Output: 2
// Example 3: Input: root = [] Output: 0

// Different Approaches:
// 1. Recursive DFS- Time O(n), Space O(n)
// 2. Iterative BFS- Time O(n), Space O(n)

// Leetcode link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
// Solution:
function TreeNode(val, left = null, right = null) {
  this.val = val;
  this.left = left;
  this.right = right;
}

function maxDepth(root) {
  if (root === null) return 0;
  let left = maxDepth(root.left);
  let right = maxDepth(root.right);
  return 1 + Math.max(left, right);
}
// Test case
const root = new TreeNode(3);
root.left = new TreeNode(9),root.right = new TreeNode(25);
root.right = new TreeNode(25);
root.right.left = new TreeNode(20, new TreeNode(15), new TreeNode(7));
console.log(maxDepth(root)); // Output: 4

// Complexity Analysis: Time O(n), Space O(n)
