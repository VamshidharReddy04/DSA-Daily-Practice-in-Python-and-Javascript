// Graphs - Number of Islands
// Given a 2D grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
// Example 1:  Input: grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]] Output: 1
// Example 2:  Input: grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"] ] // Output: 3
// Example 3:  Input: grid = [["1","1","0","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["0","0","0","0","0"],["1","0","1","1","1"]] Output: 4

// Different Approaches:
// 1. Depth First Search (DFS) - Time Complexity: O(M*N), Space Complexity: O(M*N) in worst case
// 2. Breadth First Search (BFS) - Time Complexity: O(M*N), Space Complexity: O(min(M,N))
// 3. Union-Find (Disjoint Set Union) - Time Complexity: O(M*N*α(M*N)), Space Complexity: O(M*N)
// Solution 1: Depth First Search (DFS)
// LeetCode: https://leetcode.com/problems/number-of-islands/description/
function numIslands(grid) {
    if(! grid  || grid.length ===0) return 0;
    const rows =grid.length;
    const cols=grid[0].length;
    let count=0;
    function dfs(r,c){
        if(r<0 || c<0 || r>=rows || c>=cols || grid[r][c]==='0') 
            return;
        grid[r][c]='0'; // mark as visited
        dfs(r+1,c); // down
        dfs(r-1,c); // up
        dfs(r,c+1); // right
        dfs(r,c-1); // left
    } 
    for (let r=0;r<rows;r++){      //Each Rows
        for(let c=0;c<cols;c++){   //Each Cols
            if(grid[r][c]==='1'){  // found an island
                count++;           // increment island count
                dfs(r,c);          // mark all connected cells as visited 
            }
        }
    }
    return count;
}
// Test cases
console.log(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])); // Output: 3
console.log(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","1","1"],["0","0","0","1","1"]])); // Output: 2
console.log(numIslands([["1","1","0","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["0","0","0","0","0"],["1","0","1","1","1"]])); // Output: 4

// Best Approach: Depth First Search (DFS)
// Complexity Analysis: Time Complexity: O(M*N), Space Complexity: O(M*N) in worst case
