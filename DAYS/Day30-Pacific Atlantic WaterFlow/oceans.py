# Graphs - Pacific Atlantic Water Flow
# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, 
# the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

# Example 1: Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]] Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Example 2: Input: heights = [[2,1],[1,2]] Output: [[0,0],[0,1],[1,0],[1,1]] Output: [[0,0],[0,1],[1,0],[1,1]]
# Example 3: Input: heights = [[2,2]] Output: [[0,0],[0,1],[1,0],[1,1]] Output: [[0,0],[0,1],[1,0],[1,1]]

# Different Approaches:
# 1. Brute Force (DFS from each cell) - Time O(m * n * (m + n)), Space O(m * n)
# 2. DFS/BFS from Ocean Borders - Time O(m * n), Space O(m * n)

# Solution 2: DFS from Ocean Borders
# LeetCode: https://leetcode.com/problems/pacific-atlantic-water-flow/description/
class Solution:
    @staticmethod
    def oceans(heights):
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])    # Dimensions of the matrix
        pacific, atlantic = set(), set()              # Sets to track cells reachable by each ocean
        def dfs(r, c, visited, prevHeight):
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                (r, c) in visited or heights[r][c] < prevHeight):
                return
            
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])  # Down
            dfs(r - 1, c, visited, heights[r][c])  # Up
            dfs(r, c + 1, visited, heights[r][c])  # Right
            dfs(r, c - 1, visited, heights[r][c])  # Left
            
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])          # Top row (Pacific)
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # Bottom row (Atlantic)
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])         # Left column (Pacific)
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])  # Right column (Atlantic)
                
        # Find intersection of both sets
        result = list(pacific & atlantic)
        return result
# Test Cases
print(Solution.oceans([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) # Output: [(4, 0), (0, 4), (3, 1), (1, 4), (3, 0), (2, 2), (1, 3)]
print(Solution.oceans([[2,1],[1,2]])) # Output: [[0,0],[0,1],[1,0],[1,1]]
print(Solution.oceans([[2,2]])) # Output: [[0,0],[0,1]])

# Best Approach: DFS/BFS from Ocean Borders -
# Complexity Analysis: Time O(m * n), Space O(m * n)