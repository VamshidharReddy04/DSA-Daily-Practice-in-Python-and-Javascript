# Matrix : Word Search (Leetcode-79)
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
# Example 1: Input Board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] Word = "ABCCED" Output: true
# Example 2: Input Board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] Word = "SEE" Output: true
# Example 3: Input Board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] Word = "ABCB" Output: false

# Different Approaches:
# 1. Brute Force(DFS from each cell)-Time O(m*n*4^(word_length)), Space O(1)
# 2. Optimized backtracking- Time O(m*n*4^(word_length)), Space O(word_length)

# Solution 2: Optimized backtracking
# LeetCode: https://leetcode.com/problems/word-search/solutions/310127/word-search/?orderBy=most_votes

class Solution:
    def words(board,word):
        rows ,cols =len(board),len(board[0])

        def backtrack(r,c,i):
            # Boundary mismatch Checking
            if i==len(word): return True
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c]!=word[i]: return False
            # Mark the cell as visited
            temp=board[r][c]
            board[r][c]='#'
            # Check 4 directions (left,right,up,down)
            found=backtrack(r+1,c,i+1) or backtrack(r-1,c,i+1) or backtrack(r,c+1,i+1) or backtrack(r,c-1,i+1)
            # Unmark the cell
            board[r][c]=temp
            return found
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i,j,0): return True
        return False
# Test Cases
print(Solution.words([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")) # Output: true
print(Solution.words([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE")) # Output: true
print(Solution.words([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB")) # Output: false

# Best Approach: Optimized backtracking
# Complexity Analysis: Time complexity O(m*n*4^(word_length)), Space complexity O(word_length)