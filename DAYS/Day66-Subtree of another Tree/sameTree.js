// Binary Tree : Subtree of Another Tree (LeetCode 572)\
// Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
// Example 1: Input: root = [3,4,5,1,2], subRoot = [4,1,2] Output: true
// Example 2: Input: root = [3,4,5,1,2,null,null,0], subRoot = [4,1,2] Output: false
// Different Approaches:
// 1. Recursive Comparison - Time O(N*M), Space O(H)
// 2. Tree Serialization - Time O(N+M), Space O(N+M)
// LeetCode Link: https://leetcode.com/problems/subtree-of-another-tree/
// Solution:
class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function subTree(root,subRoot){
    if(!root) return false;
    if(sameTree(root, subRoot)) return true;
    return subTree(root.left, subRoot) || subTree(root.right, subRoot);
}
function sameTree(root,subRoot){
    if(!root && !subRoot) return true;
    if(!root || !subRoot) return false;
    // nodes must have same value
    if(root.val !== subRoot.val) return false;
    return sameTree(root.left, subRoot.left) && sameTree(root.right, subRoot.right);
}

// Test Cases
const root = new TreeNode(3);
root.left = new TreeNode(4);
root.right = new TreeNode(5);
root.left.left = new TreeNode(1);
root.left.right = new TreeNode(2);
const subRoot = new TreeNode(4);
subRoot.left = new TreeNode(1);
subRoot.right = new TreeNode(2);
console.log(subTree(root,subRoot)); // true

const root2 = new TreeNode(3);
root2.left = new TreeNode(4);
root2.right = new TreeNode(5);
root2.left.left = new TreeNode(1);
root2.left.right = new TreeNode(2);
const subRoot2 = new TreeNode(null);
subRoot2.left = new TreeNode(null);
subRoot2.right = new TreeNode(0);
console.log(subTree(root2,subRoot2)); // false

// Complexity Analysis: Time complexity: O(N*M) , Space Complexity: O(H)