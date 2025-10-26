// Binary tree serialization and deserialization -LeetCode 297
// Given the root of a binary tree, serialize the tree into a string and deserialize the string back to the original tree structure.
// Example 1: Input: root = [1,2,3,null,null,4,5] Output: [1,2,3,null,null,4,5]
// Example 2: Input: root = [] Output: []
// Different Approaches: 
// 1. Preorder Traversal (DFS)- Time: O(n), Space: O(n)
// 2. Level Order Traversal (BFS)- Time: O(n), Space: O(n)
// LeetCode Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
// Solution:

class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
function serialize(root) {
    const result = [];  
    function dfs(node) {
        if (!node) {
            result.push('null');
            return;
        }
        result.push(node.val.toString());
        dfs(node.left);
        dfs(node.right);
    }
    dfs(root);
    return result.join(',');
}
function deserialize(data) {
    const values = data.split(',');
    let index = 0;
    function build() {
        if (index >= values.length) return null;
        const val = values[index++];
        if (val === 'null') return null;
        const node = new TreeNode(parseInt(val));
        node.left = build();
        node.right = build();
        return node;
    }
    return build();
}
//Test Cases
const root = new TreeNode(1, new TreeNode(2), new TreeNode(3, new TreeNode(4), new TreeNode(5)));
const serialized = serialize(root);
console.log('Serialized:', serialized);
const deserialized = deserialize(serialized);
console.log('Deserialized Root Value:', deserialized.val);

// Complexity Analysis: Time Complexity: O(n) , Space Complexity: O(n)