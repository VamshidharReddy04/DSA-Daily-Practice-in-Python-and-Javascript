// Graphs - Count the number of connected components in an undirected graph
// Given an undirected graph, count the number of connected components in the graph.
// Connected components are groups of nodes that can reach each other.
// Example 1: Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]] Output: 2
// Example 2: Input: graph = [[1,2,3,4],[1,4],[0,4],[0,1,2,3]] Output: 1

// Different Approaches:
// 1. Depth-First Search (DFS)
// 2. Breadth-First Search (BFS)
// 3. Union-Find (Disjoint Set Union - DSU)

// Solution using Depth-First Search (DFS)
// Leetcode problem link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
function countComponents(n,edges){
    const adj=Array.from({length:n},()=>[]);
    for(const [u,v] of edges){
        adj[u].push(v);
        adj[v].push(u);
    }
    const visit=new Set()
    function dfs(node){
        for(const nei of adj[node]){
            if(!visit.has(nei)){
                visit.add(nei);
                dfs(nei);
            }
        }
    }
    let components=0;
    for(let i=0;i<n;i++){
        if(!visit.has(i)){
            dfs(i);
            components++;
        }
    }
    return components;
}
// Test cases
console.log(countComponents(5,[[0,1],[1,2],[3,4]])); // Output: 2
console.log(countComponents(5,[[0,1],[1,2],[2,3],[3,4]])); // Output: 1

// Complexity Analysis: Time Complexity: O(N + E) ,Space Complexity: O(N + E)
// where N is the number of nodes and E is the number of edges in the graph.