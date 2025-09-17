# Dynamic Programming : Longest Common Subsequence
# Given two strings text1 and text2, return the length of their longest common subsequence.
# Example 1: Input: text1 = "abcde", text2 = "ace" Output: 3
# Example 2: Input: text1 = "abc", text2 = "abc" Output: 3
# Example 3: Input: text1 = "abc", text2 = "def" Output: 0

# Different Approaches:
# 1. Recursion (Brute Force)
# 2. Memoization (Top-Down DP)
# 3. Tabulation (Bottom-Up DP)
# Soultions: Bottom-Up DP
class Solution:
    def longestCommonSubsequence(self,text1,text2):
        m=len(text1) 
        n=len(text2)
        dp=[[0]*(n+1)for _ in range(m+1)] # Create a 2D array to store lengths of longest common subsequence.
        for i in range(1,m+1):   # Iterate through the text1
            for j in range (1,n+1):  # Iterate through the text2
                if text1[i-1] == text2[j-1]:  # If characters match, increment the count from the previous indices
                    dp[i][j]=1+dp[i-1][j-1]   # Increment the count from the previous indices
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])   # If characters don't match, 
                    # take the maximum count from either excluding the current character of text1 or text2
        return dp[m][n] # The bottom-right cell contains the length of the longest common subsequence.
# Test case
print(Solution().longestCommonSubsequence("abcde", "abce"))  # Output: 4
print(Solution().longestCommonSubsequence("abc", "ab"))    # Output: 2
print(Solution().longestCommonSubsequence("abc", "def"))    # Output: 0    
# Best Approach: Tabulation (Bottom-Up DP)
# Complexity Analysis: Time Complexity: O(m*n), Space Complexity: O(m*n)

# 1. Recursion (Brute Force)

def lcs_recursive(text1, text2):
    if len(text1) == 0 or len(text2) == 0:
        return 0
    if text1[-1] == text2[-1]:
        return 1 + lcs_recursive(text1[:-1], text2[:-1])
    else:
        return max(lcs_recursive(text1[:-1], text2),   
            lcs_recursive(text1, text2[:-1]))
# Test case
print(lcs_recursive("abcde", "ace"))  # Output: 3
print(lcs_recursive("abc", "abc"))    # Output: 3
print(lcs_recursive("abc", "def"))    # Output: 0
# Complexity Analysis: Time Complexity: O(2^(m+n)), Space Complexity: O(m+n)

# 2. Memoization (Top-Down DP)
def lcs_memoization(text1, text2):
    memo = {}
    if len(text1) == 0 or len(text2) == 0:
        return 0
    if (text1, text2) in memo:
        return memo[(text1, text2)]
    if text1[-1] == text2[-1]:
        memo[(text1, text2)] = 1 + lcs_memoization(text1[:-1], text2[:-1])
        return memo[(text1, text2)]
    else:
        memo[(text1, text2)] = max(lcs_memoization(text1[:-1], text2),   
            lcs_memoization(text1, text2[:-1]))
        return memo[(text1, text2)]
# Test case 
print(lcs_memoization("abcde", "ace"))  # Output: 3
print(lcs_memoization("abc", "abc"))    # Output: 3 
print(lcs_memoization("abc", "def"))    # Output: 0

# Complexity Analysis: Time Complexity: O(m*n), Space Complexity: O(m*n)