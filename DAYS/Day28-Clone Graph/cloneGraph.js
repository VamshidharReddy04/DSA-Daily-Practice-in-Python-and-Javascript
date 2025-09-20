// Graphs - Clone Graph
// Problem Statement: Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
// Example 1:
// Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
// Output: [[2,4],[1,3],[2,4],[1,3]] 

// Different Approaches:
// 1. DFS using Recursion - Time: O(N) Space: O(N)
// 2. DFS using Stack - Time: O(N) Space: O(N)
// 3. BFS using Queue - Time: O(N) Space: O(N)

// Solution 3: BFS using Queue
function Node(val, neighbors) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
}
var cloneGraph = function(node) {
    if(!node) return node;
    const map = new Map();
    const queue = [node];
    map.set(node, new Node(node.val));
    while(queue.length) {
        const curr = queue.shift();
        for (const nei of curr.neighbors) {
            if (!map.has(nei)) {
                map.set(nei, new Node(nei.val));
                queue.push(nei);
            }
            map.get(curr).neighbors.push(map.get(nei));
        }
    }
    return map.get(node);
};
// Test Cases:
console.log(cloneGraph(new Node(1, [new Node(2), new Node(4)]))); 
console.log(cloneGraph([[2,4],[1,3],[2,4],[1,3]])); 
// Approach used: BFS using Queue
// Complexity Analysis: Time Complexity: O(N) Space Complexity: O(N)