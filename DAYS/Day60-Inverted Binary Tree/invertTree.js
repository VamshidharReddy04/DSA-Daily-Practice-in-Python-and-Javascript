// Binary Tree Inversion - Invert a binary tree. leetcode 226
// given the root of a binary tree, invert the tree, and return its root.
// Example 1: input: root = [4,2,7,1,3,6,9] output: [4,7,2,9,6,3,1]
// Example 2: input: root = [2,1,3] output: [2,3,1]

// Different Approaches:
// 1. Recursive DFS - Time: O(n), Space: O(n)
// 2. Iterative Approach using Queue (BFS) - Time: O(n), Space: O(n)
// 3. Iterative Approach using Stack (DFS) - Time: O(n), Space: O(n)
// Leetcode Link: https://leetcode.com/problems/invert-binary-tree/
// Solution 1: Recursive DFS

function invertTree(root){
    if(!root) return null;
    [root.left, root.right] = [invertTree(root.right), invertTree(root.left)];
    return root;
}
// Test Cases
// Case 1
let root1 = [4,2,7,1,3,6,9];
console.log(invertTree(root1)); // [4,7,2,9,6,3,1]
// Case 2
let root2 = [2,1,3];
console.log(invertTree(root2)); // [2,3,1]

// Solution 2: Iterative Approach using Queue (BFS)

function invertTreeBFS(root){
    if (!root) return null;
    let res=[];
    let queue=[root];
    while(queue.length){
        const node=queue.shift(); //shift() remove frist element
        if (node) {
            res.push(node);
            queue.push(node.left);
            queue.push(node.right);
        }else{
            res.push(null);
        }
    }
    return res;
}
// Test Cases
let root3 = [4,2,7,1,3,6,9];
console.log(invertTreeBFS(root3)); // [4,7,2,9,6,3,1]
let root4 = [2,1,3];
console.log(invertTreeBFS(root4)); // [2,3,1]

// Best Approach: both have same Complexity Analysis: Time Complexity: O(n) Space Complexity: O(n)