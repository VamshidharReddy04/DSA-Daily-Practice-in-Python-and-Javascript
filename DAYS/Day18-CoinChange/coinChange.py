# Dynamic programming : Coin Change Problem
# Given a set of coin denominations and a target amount, 
# find the minimum number of coins needed to make up that amount.
# If it is not possible to make up the target amount, return -1.
# Example 1: Input: coins = [1, 2, 5], amount = 11 Output: 3 (11 = 5 + 5 + 1)
# Example 2: Input: coins = [2], amount = 3 Output: -1
# Different Approaches:
# 1. Recursive Approach (Brute Force)
# 2. Dynamic Programming (Top-Down with Memoization)
# 3. Dynamic Programming (Bottom-Up Approach) - Best Approach
# Leetcode : https://leetcode.com/problems/coin-change/

# Bottom-Up Dynamic Programming Approach (Best)
class Solution:
    def coinChange(self,coins,amount):
        dp=[float('inf')]*(amount + 1) # Initialize dp array with infinity
        dp[0]=0      # Base case: 0 coins are needed to make amount 0
        for i in range(1,amount +1): 
            for coin in coins:      # Iterate through each coin denomination
                if i-coin >=0:      # Check if the remaining amount is greater than or equal to the current coin
                    dp[i]=min(dp[i],dp[i-coin]+1) # Update dp[i] with the minimum coins needed to make amount i
        return dp[amount] if dp[amount]!=float('inf') else -1 # Return the minimum coins needed to make amount amount.
                 
# Test Case :
print(Solution().coinChange([1,2,5],11)) # Output: 3
print(Solution().coinChange([2],3))       # Output: -1

# Best Approach: Bottom-Up
# Complexity Analysis: Time Complexity O(N*M) , Space Complexity O(N)


# Approach 1: Brute-force Recursive Approach
class BruteForceSolution:
    @staticmethod
    def coinChange(coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        minCoins = float('inf')
        for coin in coins:
            numCoins = 1 + BruteForceSolution.coinChange(coins, amount - coin)
            minCoins = min(minCoins, numCoins)
        return minCoins if minCoins != float('inf') else -1

# Test Case :
print(BruteForceSolution.coinChange([1, 2, 5], 11)) # Output: 3
print(BruteForceSolution.coinChange([2], 3))        # Output: 1
print(BruteForceSolution.coinChange([1], 0))        # Output: 0

# Complexity Analysis: Time Complexity O(N^M) , Space Complexity O(M)


# Approach 2: Top-Down with Memoization
class MemoizedSolution:
    @staticmethod
    def coinChange(coins, amount, memo=None):
        if memo is None:
            memo = {}
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        minCoins = float('inf')
        for coin in coins:
            numCoins = 1 + MemoizedSolution.coinChange(coins, amount - coin, memo)
            minCoins = min(minCoins, numCoins)
        memo[amount] = minCoins
        return minCoins if minCoins != float('inf') else -1

# Test Case :
print(MemoizedSolution.coinChange([1, 2, 5], 11)) # Output: 3
print(MemoizedSolution.coinChange([2], 3))        # Output: -1
print(MemoizedSolution.coinChange([1], 0))        # Output: 0

# Complexity Analysis: Time Complexity O(N*M) , Space Complexity O(M)
