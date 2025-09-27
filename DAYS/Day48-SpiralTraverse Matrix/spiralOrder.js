// Matrix - Spiral Order Traversal
// Given an m x n matrix, return all elements of the matrix in spiral order.
// Example 1: Input: matrix = [[1,2,3],[4,5,6],[7,8,9]] Output: [1,2,3,6,9,8,7,4,5]
// Example 2: Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] Output: [1,2,3,4,8,12,11,10,9,5,6,7]
// Different Approaches:
// 1. Brute Force (Marked Matrix)-Time: O(m*n), Space: O(m*n)
// 2.Optimal (Boundary Tracking)-Time: O(m*n), Space: O(1)
// SOlution: Optimal (Boundary Tracking)
// Leetcode: https://leetcode.com/problems/spiral-matrix/description/
function spiralOrder(matrix) {
    if (matrix.length === 0) return [];
    const result = [];
    let top = 0;
    let bottom = matrix.length - 1;
    let left = 0;
    let right = matrix[0].length - 1;
    while(top<=bottom && left<=right){
        // Traverse TopRow from left to right
        for(let i=left; i<=right; i++){
            result.push(matrix[top][i]);
        }
        top++;
        // Traverse RightCol from top to bottom
        for(let i=top; i<=bottom; i++){
            result.push(matrix[i][right]);
        }
        right--;
        if (top <= bottom) {
            // Traverse BottomRow from right to left
            for(let i=right; i>=left; i--){
                result.push(matrix[bottom][i]);
            }
            bottom--;
        }
        if (left <= right) {
            // Traverse LeftCol from bottom to top
            for(let i=bottom; i>=top; i--){
                result.push(matrix[i][left]);
            }
            left++;
        }
    }
    return result;
}
// Test Cases
console.log(spiralOrder([[1,2,3],[4,5,6],[7,8,9]])); // Output- [1,2,3,6,9,8,7,4,5]
console.log(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])); // Output- [1,2,3,4,8,12,11,10,9,5,6,7]

// Best Approach- Boundary Tracking
// Complexity Analysis: Time Complexity: O(m*n), Space Complexity: O(1)