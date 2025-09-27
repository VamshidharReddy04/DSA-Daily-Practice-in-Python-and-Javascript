# Matrix - Spiral Order Traversal
# Given an m x n matrix, return all elements of the matrix in spiral order.
# Example 1: Input: matrix = [[1,2,3],[4,5,6],[7,8,9]] Output: [1,2,3,6,9,8,7,4,5]
# Example 2: Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# Different Approaches: 
# 1. Brute Force (mark visited )- Time: O(m*n), Space: O(m*n)
# 2. Optimized Approach (Boundary Tracking)- Time: O(m*n), Space: O(1)

# Solution 2: Optimized Approach (Boundary Tracking)
# LeetCode: https://leetcode.com/problems/spiral-matrix/description/
class Solution:
    def spiralOrder(matrix):
        if not matrix:
            return []
        result = []
        top, bottom, left, right = 0,len(matrix)-1,0,len(matrix[0])-1
        while top<=bottom and left<=right:
            # Traverse top row
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1
            # Traverse right column
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right-=1
            if top<=bottom:
                # Traverse bottom row (right to left)
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom-=1
            if left<=right:
                # Traverse left column (bottom to top)
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left+=1
        return result
# Test Cases
print(Solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
print(Solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]
# Best Approach: Boundary Tracking
# Complexity Analysis: Time Complexity: O(m*n), Space Complexity: O(1)