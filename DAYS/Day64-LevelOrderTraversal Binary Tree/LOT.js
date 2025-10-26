// Binary tree Level Order Traversal- leetcode 102
// Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
// Example 1: Input: root = [3,9,20,null,null,15,7] Output: [[3],[9,20],[15,7]]
// Example 2: Input: root = [1] Output: [[1]]
// Different approach :
// 1. Using BFS with a queue- Time O(n), Space O(n)
// 2. Using DFS with recursion- Time O(n), Space O(h) 

// Leetcode link: https://leetcode.com/problems/binary-tree-level-order-traversal/
// Solution:

class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
// BFS approach
function levelOrderBFS(root) {
    if (!root) return [];
    let res=[];
    let queue=[root];
    while(queue.length){
        let level=[];
        let size=queue.length;
        for(let i=0;i<size;i++){
            let node=queue.shift();
            level.push(node.val);
            if(node.left)queue.push(node.left);
            if(node.right)queue.push(node.right);
        }
        res.push(level);    
    }
    return res;
}
// Test cases
let root1 = new TreeNode(3);
root1.left = new TreeNode(9);
root1.right = new TreeNode(2);
root1.right.left = new TreeNode(10);
root1.right.right = new TreeNode(7);
let root2 = new TreeNode(1);
console.log(levelOrderBFS(root1)); // Output: [[3],[9,2],[10,7]]
console.log(levelOrderBFS(root2)); // Output: [[1]] 

// Complexity Analysis: Time Complexity: O(n) , Space Complexity: O(n)