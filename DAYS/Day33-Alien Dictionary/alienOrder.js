//Graphs- Alien Dictionary Order
//Given a list of words from the alien language dictionary, where the words are sorted lexicographically by the rules of this new language, derive the order of letters in this language.

//Example 1: Input: words = ["wrt","wrf","er","ett","rftt"] Output: "wertf"
//Example 2: Input: words = ["z","x"] Output: "zx"
//Example 3: Input: words = ["z","x","z"] Output: "" Explanation: The order is invalid, so return "".
// Different Approach: 
// 1. DFS Topological Sort
// 2. BFS Topological Sort (Kahn's Algorithm)

// Solution: BFS Topological Sort (Kahn's Algorithm)
// Leetcode: https://leetcode.com/problems/alien-dictionary/solutions/1678823/javascript-bfs-topological-sort-kahn-s-algorithm-with-detailed-explanation/?orderBy=most_relevant

function alienOrder(words){
    if(!words ||words.length ===0) return "";

    // Step 1: Create the graph
    const graph = new Map();
    const indegree = new Map();
    for(let word of words){
        for(let ch of word){
            if(!graph.has(ch)) graph.set(ch,new Set());
            if(!indegree.has(ch)) indegree.set(ch,0);
        }
    }
    // Step 2: Build the graph
    for(let i=0;i<words.length-1;i++){
        const w1=words[i];
        const w2=words[i+1];
        if(w1.length>w2.length && w1.startsWith(w2)) return ""; // Invalid case
        const minLength=Math.min(w1.length,w2.length);
        for(let j=0;j<minLength;j++){
            if(w1[j]!==w2[j]){ // Find the first different character
                if(!graph.get(w1[j]).has(w2[j])){   // Avoid duplicate edges
                    graph.get(w1[j]).add(w2[j]); // Add edge
                    indegree.set(w2[j],indegree.get(w2[j])+1); // Increase indegree
                    break; // Only the first different character between the two words will help us find the order
                }
            }
        }
    }
    // Step 3: Topological Sort using BFS (Kahn's Algorithm)
    const queue = [];
    for(let [key,value] of indegree.entries()){
        if(value===0) queue.push(key); // Start with nodes with 0 indegree
    }   
    const result = [];
    while(queue.length>0){
        const ch = queue.shift();
        result.push(ch);
        for(let neighbor of graph.get(ch)){
            indegree.set(neighbor,indegree.get(neighbor)-1); // Decrease indegree
            if(indegree.get(neighbor)===0) queue.push(neighbor); // If indegree becomes 0, add to queue
        }
    }
    return result.length===indegree.size ? result.join('') : ''; // If result length is not equal to indegree size, there is a cycle
}

// Test Cases
console.log(alienOrder(["wrt","wrf","er","ett","rftt"])); // Output: "wertf"
console.log(alienOrder(["z","x"])); // Output: "zx"
console.log(alienOrder(["z","x","z"])); // Output: ""
// Best Approach: BFS Topological Sort (Kahn's Algorithm)
// Complexity Analysis: Time Complexity- O(v+e) , Space Complexity- O(v+e) 
// where v is the number of unique characters and e is the number of edges in the graph.