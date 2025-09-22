// Graphs - Pacific Atlantic Water Flow
// Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
// Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
// Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
// Example 1: Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]] Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
// Example 2: Input: heights = [[2,1],[1,2]] Output: [[0,0],[0,1],[1,0],[1,1]]
// Different Approaches:
// 1. DFS/BFS from Each Cell - Time O(m * n * (m + n)), Space O(m * n)
// 2. DFS/BFS from Ocean Borders - Time O(m * n), Space O(m * n)

// Solution 2: DFS from Ocean Borders
// LeetCode: https://leetcode.com/problems/pacific-atlantic-water-flow/description/

function oceans(heights) {
    if(!heights || heights.length === 0) return [];  // Matrix is empty
    const rows = heights.length;
    const cols = heights[0].length;
    const pacific = new Set();
    const atlantic = new Set();
    
    function dfs(r, c, visited, prevHeight) {
        if(r < 0 || c < 0 || r >= rows || c >= cols || 
           visited.has(`${r},${c}`) || heights[r][c] < prevHeight) {
            return;
        }
        
        visited.add(`${r},${c}`); // Mark cell as visited
        dfs(r + 1, c, visited, heights[r][c]); // Down
        dfs(r - 1, c, visited, heights[r][c]); // Up
        dfs(r, c + 1, visited, heights[r][c]); // Right
        dfs(r, c - 1, visited, heights[r][c]); // Left
    }
    
    // DFS from Pacific borders (top row and left column)
    for(let c = 0; c < cols; c++) {
        dfs(0, c, pacific, heights[0][c]);          // Top row (Pacific)
        dfs(rows - 1, c, atlantic, heights[rows - 1][c]);  // Bottom row (Atlantic)
    }
    for(let r = 0; r < rows; r++) {
        dfs(r, 0, pacific, heights[r][0]);         // Left column (Pacific)
        dfs(r, cols - 1, atlantic, heights[r][cols - 1]);  // Right column (Atlantic)
    }
    
    // Find intersection of cells reachable by both oceans
    const result = [];
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (pacific.has(`${r},${c}`) && atlantic.has(`${r},${c}`)) {
                result.push([r, c]);
            }
        }
    }
    return result;
}
 
// Test Cases
console.log(oceans([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) // Output: [(4, 0), (0, 4), (3, 1), (1, 4), (3, 0), (2, 2), (1, 3)]
console.log(oceans([[2,1],[1,2]])) // Output: [[0,0],[0,1],[1,0],[1,1]]
console.log(oceans([[2,2]])) // Output: [[0,0],[0,1]]
    
// Best Approach: DFS/BFS from Ocean Borders -
// Complexity Analysis: Time O(m * n), Space O(m * n)
