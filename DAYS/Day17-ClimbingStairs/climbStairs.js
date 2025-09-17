// Dynamic Programming : Climbing Stairs
// Given n stairs, you can climb either 1 or 2 stairs at a time.
// Write a function to count the number of distinct ways to reach the top.
// Example: Input: n = 1, Output: 1 (1 way to climb 1 stair)
// Example: Input: n = 3, Output: 3 (1+1+1, 1+2, 2+1)
// Example: Input: n = 4, Output: 5 (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)
// Example: Input: n = 45, Output: 1836311903
function climbStairs(n) {
    if (n <= 1) return 1;
    let dp = new Array(n + 1);
    dp[0] = 1; // 1 way to stay at the ground (do nothing)
    dp[1] = 1; // 1 way to reach the first step
    for (let i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2]; // Sum of ways to reach the last step and the step before last
    }
    return dp[n];
}
// Test cases
console.log(climbStairs(1)); // 1
console.log(climbStairs(3)); // 3
console.log(climbStairs(4)); // 5
console.log(climbStairs(45)); // 1836311903

// Best Approach: Optimized Dynamic Programming
// Complexity Analysis: Time Complexity: O(n), Space Complexity: O(1)