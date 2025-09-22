# Graphs - Number of Islands
# Given a 2D grid map of '1's (land) and '0's (water), count the number of islands.
# Example 1: Input: grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
# Output: 3
# Example 2: Input: grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","1","1"],["0","0","0","1","1"]]
# Output: 2
# Different approaches: 
# 1. Depth-First Search (DFS) - O(M*N) time, O(M*N) space
# 2. Breadth-First Search (BFS) - O(M*N) time, O(min(M,N)) space
# 3. Union-Find - O(M*N) time, O(M*N) space

# Solution - DFS
# Leetcode: https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self,grid):
        if not grid: return 0   
        rows,cols=len(grid),len(grid[0])
        count=0

        def dfs(r,c):
            if r<0 or c<0 or r>rows-1 or c>cols-1 or grid[r][c]=='0': 
                return
            grid[r][c]='0'
            dfs(r+1,c) # down
            dfs(r-1,c) # up
            dfs(r,c+1) # right
            dfs(r,c-1) # left
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1': # found an island
                    dfs(r,c)  # mark all connected cells as visited
                    count +=1 # increment island count
        return count    # return island count
# Test cases
print(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])) # Output: 3
print(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","1","1"],["0","0","0","1","1"]])) # Output: 2     

# Best Solution - DFS
# complexity - Time:O(M*N) Space: O(M*N) 