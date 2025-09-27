#  Matrix- Rotate Matrix based 2D rotation transformation
# Given an n x n matrix, rotate it by 90 degrees clockwise.
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
# Example 1: Input: matrix = [[1,2,3],[4,5,6],[7,8,9]] Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2: Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# Different Approaches:
# 1. Transpose and Reverse: Time Complexity: O(n^2) Space Complexity: O(1)
# 2. Layer by Layer Rotation: Time Complexity: O(n^2) Space Complexity: O(1)

# Solution 1: Transpose and Reverse
# Leetcode: https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(matrix):
        n=len(matrix)
        # Transpose the matrix
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for i in range(n):
            matrix[i].reverse()
        return matrix
# Test Cases
print(Solution.rotate([[1,2,3],[4,5,6],[7,8,9]])) # Output: [[7,4,1],[8,5,2],[9,6,3]]
print(Solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])) 
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# Best Approach: Transpose and Reverse
# Complexity Analysis: Time Complexity: O(n^2) Space Complexity: O(1)