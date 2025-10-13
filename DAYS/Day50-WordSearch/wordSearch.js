// Matrix : Word Search (Leetcode-)
// Given an m x n grid of characters board and a string word, return true if word exists in the grid.
// The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
// Example 1: Input Board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] Word = "ABCCED" Output: true
// Example 2: Input Board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] Word = "SEE" Output: true
// Example 3: Input Board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] Word = "ABCB" Output: false

// Different Approaches:
// 1. Brute Force - Time O(m*n*4^L) Space O(L) 
// 2. Backtracking - Time O(m*n*3^L) Space O(L)

// Solution 2 : Backtracking
// Leetcode : https://leetcode.com/problems/word-search/solutions/29278/clean-java-backtracking-solution-with-explanation/

function exist(board, word) {
    const rows = board.length;
    const cols = board[0].length;

    function back(r,c,i){
        if(i==word.length) return true;
        if(r<0 || c<0 || r>=rows ||c>=cols || board[r][c] !==word[i]) return false;
        // Mark cells
        const temp=board[r][c];
        board[r][c]='#';
        // Mark 4 direction
        const found = back(r+1,c,i+1) || // down
        back(r-1,c,i+1) || // up
        back(r,c+1,i+1) || // right
        back(r,c-1,i+1); // left

        board[r][c]=temp;
        return found
    }
    for(let i=0;i<rows;i++){
        for(let j=0;j<cols;j++){
            if(back(i,j,0)) return true;
        }
    }
    return false;
}

// Test Cases
const board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]];
console.log(exist(board.map(r=>r.slice()), "ABCCED")); // true
console.log(exist(board.map(r=>r.slice()), "SEE")); // true
console.log(exist(board.map(r=>r.slice()), "ABCB")); // false

// Best Approach : Optimized Backtracking
// Complexity Analysis: Time complexity O(n*m*4^L) ,Space Complexity O(L)