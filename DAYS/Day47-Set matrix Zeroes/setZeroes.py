#  Matrix - Set Matrix Zeroes (LeetCode 73)
# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
# Example 1: Input: matrix = [[1,1,1],[1,0,1],[1,1,1]] Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2: Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]] Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# Different Approaches:
# 1. Brute Force: Time O(mn) Space O(mn)
# 2. Row and Column: Time O(mn) Space O(m+n)
# 3. Optimal In-place Approach: Time O(mn) Space O(1)

# Solution 3: Optimal In-place Approach
# LeetCode Link: https://leetcode.com/problems/set-matrix-zeroes/description/
class Solution:
    def setZeroes(self,matrix):
        rows,cols=len(matrix),len(matrix[0])
        firstRowZero,firstColZero=False ,False
        # Mark rows and cols zero
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:        # Found a zero
                    if r==0:        # First Row
                        firstRowZero=True   # Marking first row zero
                    if c==0:        # First Column
                        firstColZero=True   # Marking first column zero
                    matrix[0][c]=0
                    matrix[r][0]=0
        # Update row and column
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0   # Marking row and column zero

        # Update First row
        if firstRowZero:
            for c in range(cols): 
                matrix[0][c]=0      # Update First Row
        # Update First Column
        if firstColZero:
            for r in range(rows):
                matrix[r][0]=0    # Update First Column
        return matrix
# Test Case
print(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]])) # Output: [[1,0,1],[0,0,0],[1,0,1]]
print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])) # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Best Approach: Optimal In-place Approach
# Complexity Analysis: Time Complexity: O(mn) , Space Complexity: O(1)
# Where m is the number of rows and n is the number of columns in the matrix. 