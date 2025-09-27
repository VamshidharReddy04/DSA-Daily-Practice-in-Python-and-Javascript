// Matrix - Set Matrix Zeroes (LeetCode 73)
// Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
// Example 1: Input: matrix = [[1,1,1],[1,0,1],[1,1,1]] Output: [[1,0,1],[0,0,0],[1,0,1]]
// Example 2: Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]] Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
// Different Approaches:
// 1. Brute Force: Time O(mn), Space O(mn)
// 2. Rows and Columns: Time O(mn), Space O(m+n)
// 3. Optimal In-place Approach: Time O(mn), Space O(1)

// Solution 3 : Optimal In-place Approach
//LeetCode : https://leetcode.com/problems/set-matrix-zeroes/description/

function setZeroes(matrix){
    let rows=matrix.length,cols=matrix[0].length;
    let firstRowsZero=false,firstColsZero=false;
    // Mark rows and cols zero
    for(r=1;r<rows;r++){
        for(c=1;c<cols;c++){
            if(matrix[r][c]==0){  // Found a zero
                firstRowsZero=true; // Marking first row zero
                firstColsZero=true; // Marking first column zero    
            }
            matrix[0][c]=0;     // Marking column zero
            matrix[r][0]=0;    // Marking row zero
        }
        // Update row and column
        if(matrix[r][0]==0 || matrix[0][c]==0){
            matrix[r][c] =0; // Marking row and column zero
        }
    }
    //Update FirstRow
    if(firstRowsZero){
        for(c=0;c<cols;c++){
            matrix[0][c]=0;  // Marking first row zero
        }
    }
    //Update FirstColumn
    if(firstColsZero){
        for(r=0;r<rows;r++){
            matrix[r][0]=0; // Marking first column zero
        }
    }
    return matrix;
}
// Test Case
console.log(setZeroes([[1,1,1],[1,0,1],[1,1,1]])); // Output: [[1,0,1],[0,0,0],[1,0,1]]
console.log(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])); // Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

// Best Approach: Optimal In-place Approach: 
// Complexity Analysis: The time complexity is O(mn) , Space Complexity is O(1)