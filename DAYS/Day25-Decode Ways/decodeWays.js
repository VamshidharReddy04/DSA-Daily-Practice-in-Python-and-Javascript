// Dynamic Programming  : Decode Ways
// Given a string s containing only digits, return the number of ways to decode it.
// The mapping is 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26.
// Example 1: Input: s = "12" Output: 2
// Example 2: Input: s = "226" Output: 3
// Example 3: Input: s = "06" Output: 0

// Different Approaches : 
// 1. Recursion (Brute Force) : O(2^n) time | O(n) space
// 2. Recursion + Memoization : O(n) time | O(n) space
// 3. Dynamic Programming (Tabulation) : O(n) time | O(n) space
// 4. Dynamic Programming (Space Optimization) : O(n) time | O(1) space

// Solution 4 : Space Optimization

function decodeWays(s) {
    if (!s || s[0] === '0') return 0; // Edge case: empty string or starts with '0'
    const n = s.length;
    let dp = new Array(n + 2).fill(0); // Create a dp array of size n+2
    dp[n] = 1; // Base case: empty string has one way to decode
    for (let i = n - 1; i >= 0; i--) {
        if (s[i] === '0') { // If the current character is '0', there are no ways to decode it
            dp[i] = 0;     
        } else {
            dp[i] = dp[i + 1]; // Single digit decode
            if (i + 1 < n && parseInt(s.substring(i, i + 2)) >= 10 && parseInt(s.substring(i, i + 2)) <= 26) {
                dp[i] += dp[i + 2]; // Two digit decode
            }
        }
    }
    return dp[0]; // Return the number of ways to decode the string
}  
// Test Cases
console.log(decodeWays("226")); // Output: 3
console.log(decodeWays("12")); // Output: 2
console.log(decodeWays("06")); // Output: 0

// Best Approach : Space Optimization
// Complexity Analysis : Time Complexity O(n) | Space Complexity O(1)