// Dynamic Programming : Coin Change Problem
// Given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money,
// return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
// You may assume that you have an infinite number of each kind of coin.
// Example 1: Input: coins = [1,2,5], amount = 11 Output: 3 (11 = 5 + 5 + 1)
// Example 2: Input: coins = [2], amount = 3 Output: -1
// Example 3: Input: coins = [1], amount = 0 Output: 0

function coinChange(coins, amount) {
    const dp = new Array(amount + 1).fill(Infinity);
    dp[0] = 0; // Base case: 0 coins are needed to make amount 0
    for (let coin of coins) { // Iterate through each coin
        for (let x = coin; x <= amount; x++) {
            dp[x] = Math.min(dp[x], dp[x - coin] + 1);
        }
    }
    return dp[amount] === Infinity ? -1 : dp[amount];
}   
// Test cases
console.log(coinChange([1, 2, 5], 11)); // Output: 3
console.log(coinChange([2], 3)); // Output: -1
console.log(coinChange([1], 0)); // Output: 0

// Best Approach: Dynamic Programming
// Complexity Analysis: Time Complexity: O(S*n) , Space Complexity: O(S)