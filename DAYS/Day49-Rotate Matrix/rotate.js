// Matrix- Rotate Matrix based 2D rotation transformation
// Given an n*n matrix, rotate the matrix by 90 degrees (clockwise).
// You have to rotate the matrix in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
// Example 1: Input: [[1,2,3],[4,5,6],[7,8,9]] Output: [[7,4,1],[8,5,2],[9,6,3]]
// Example 2: Input: [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

// Different Approaches:
// 1. Transpose and Reverse - Time: O(n^2), Space: O(1)
// 2. Brute Force - Time: O(n^2), Space: O(n^2)
// Solution- Transpose and Reverse
// LeetCode: https://leetcode.com/problems/rotate-image/
function rotate(matrix) {
    const n = matrix.length;
    for (let i = 0; i < n; i++) {
        for (let j = i; j < n; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
    }
    for (let i = 0; i < n; i++) {
        matrix[i].reverse();
    }
    return matrix;
}
// Test cases
console.log(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])); // Output: [[7,4,1],[8,5,2],[9,6,3]]
console.log(rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])); 
// Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

// Best Approach- Transpose and Reverse
// Complexity Analysis-Time Complexity: O(n^2) ,Space Complexity: O(1)