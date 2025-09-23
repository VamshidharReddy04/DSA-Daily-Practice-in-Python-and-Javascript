// Graphs- Valid Tree
// Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
// Example 1: Input: n = 5, edges = [[0,1], [0,2], [0,3], [1,4], [2,4]] Output: true
// Example 2: Input: n = 5, edges = [[0,1], [1,2], [2,3], [1,3], [1,4]] Output: false
// Example 3: Input: n = 0, edges = [] Output: true

// Differnt Approaches:
// 1.DFS / BFS to detect cycle and check connectivity
// 2.Union-Find to detect cycle and check connectivity

// Solution 1: DFS / BFS
// LeetCode: https://leetcode.com/problems/graph-valid-tree/description/
// LintCode: https://www.lintcode.com/problem/graph-valid-tree/description
function vaildTree(n,edges){
    if(n==0) return true;
    const adj=new Array(n).fill(0).map(()=>[]);
    for(const [u,v] of edges){
        adj[u].push(v);
        adj[v].push(u);
    }
    const visited=new Set();
    function dfs(nodes,parent){
        visited.add(nodes);
        for(const node of adj[nodes]){
            if(node==parent) continue;
            if(visited.has(node)) return false;
            if(!dfs(node,nodes)) return false;
        }
        return true;
    }
    return dfs(0,-1);
}
// Test Cases:
console.log(vaildTree(5, [[0,1], [0,2], [0,3], [1,4]])); // true
console.log(vaildTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]])); // false
console.log(vaildTree(0, [])); // true

// Best Approach : DFS / BFS
// Complexity Analysis: Time Complexity: O(n) Space Complexity: O(n)