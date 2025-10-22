// String - Palindrome Substring
// Given a string s, return the number of palindromic substrings in it.
// Example 1: Input: "abc" Output: 3
// Example 2: Input: "aaa" Output: 6

// Different Approaches:
// 1. Brute Force Approach- Time O(N^3) Space O(1)
// 2. Dynamic Programming- Time O(N^2) Space O(N^2)
// 3. Expand Around Center- Time O(N^2) Space O(1)

// Leetcode Link: https://leetcode.com/problems/palindromic-substrings/
// Solution:
function countSubstrings(s) {
    let count = 0;
    const expand = (left, right) => {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            count++;
            left--;
            right++;
        }
    };
    for (let i = 0; i < s.length; i++) {
        expand(i, i);     // Odd Length Palindrome
        expand(i, i + 1); // Even Length Palindrome
    }
    return count;
}
// Test Cases
console.log(countSubstrings("abc")); // Output: 3
console.log(countSubstrings("aaa")); // Output: 6
// Best Approach: Expand Around Center
// Complexity Analysis: Time Complexity: O(N^2) Space Complexity: O(1)