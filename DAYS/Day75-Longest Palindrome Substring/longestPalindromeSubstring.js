// Dynamic Programming : Longest Palindromic Substring (Leetcode 5)
// Given a string s, find the length of the longest palindromic substring.
// Example 1: Input: s = "babad" Output: 5
// Example 2: Input: s = "cbbd" Output: 2
// Example 3: Input: s = "a" Output: 1
// Different Approaches:
// 1. Brute Force Approach -Time O(n^3) Space O(1)
// 2. Dynamic Programming Approach - Time O(n^2) Space O(n^2)
// 3. Expand Around Center Approach - Time O(n^2) Space O(1)
// 4. Manacher's Algorithm - Time O(n) Space O(n)

// Leetcode Link: https://leetcode.com/problems/longest-palindromic-substring/
function longestPalindrome(s) {
    const n = s.length;
    if (n === 0) return "";
    let start = 0, maxLength = 1;
    const dp = Array.from({ length: n }, () => Array(n).fill(false));
    for (let i = 0; i < n; i++) {
        dp[i][i] = true;
    }
    for (let length = 2; length <= n; length++) {
        for (let i = 0; i < n - length + 1; i++) {
            const j = i + length - 1;
            if (s[i] === s[j]) {
                if (length === 2 || dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    if (length > maxLength) {
                        start = i;
                        maxLength = length;
                    }
                }
            }   
        }
    }   
    return s.substring(start, start + maxLength);
}
// Test Cases
console.log(longestPalindrome("babad")); // Output: "bab" or "aba"
console.log(longestPalindrome("cbbd")); // Output: "bb"
console.log(longestPalindrome("a")); // Output: "a"
console.log(longestPalindrome("ac")); // Output: "a" or "c"

// Best Approach: Manacher's Algorithm
// Complexity Analysis: Time complexity is O(n) and Space complexity is O(n)