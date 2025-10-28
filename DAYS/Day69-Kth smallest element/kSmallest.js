// Binary Tree- Kth Smallest Element in a BST (Leetcode 230)
// Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
// Example 1:Input: root = [3,1,4,null,2], k = 1 Output: 1
// Example 2:Input: root = [5,3,6,2,4,null,null,1], k = 3 Output: 3
// Different Approaches:
// 1. Inorder Traversal (Recursive)- Time O(N), Space O(N)
// 2. Min-Heap Approach - Time O(N log K), Space O(K)
// Leetcode Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
// Solution:

function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
function kSmallest(root, k) {
    let stack = [];
    let current = root;
    let count = 0;
    while (stack.length > 0 || current !== null) {
        while (current !== null) {
            stack.push(current);  // Push left nodes onto stack
            current = current.left; // Go to leftmost node
        }
        current = stack.pop(); // Visit the node
        count++;
        if (count === k) {
            return current.val;  // Found the kth smallest element
        }
        current = current.right; // Move to the right subtree
    }
    return -1; // This line should never be reached if k is valid
}
// Test Case:
let root=new TreeNode(5);
root.left=new TreeNode(3);
root.right=new TreeNode(6);
root.left.left=new TreeNode(2);
root.left.right=new TreeNode(4);
root.left.left.left=new TreeNode(1);    
let k=3;
console.log(kSmallest(root,k)); // Output: 3

let root2=new TreeNode(3);
root2.left=new TreeNode(1);
root2.right=new TreeNode(4);
root2.left.right=new TreeNode(2);
let k2=1;
console.log(kSmallest(root2,k2)); // Output: 1

// Complexity Analysis: Time Complexity: O(H), Space Complexity: O(H) 