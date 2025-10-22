// Strings - Valid Palindrome Leetcode 125
// Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
// Example 1: Input: s = "A man, a plan, a canal: Panama" Output: true
// Example 2: Input: s = "race a car" Output: false
// Different Approaches: 
// 1. Two Pointer Approach- Time O(n), Space O(1)
// 2. String Reversal Approach- Time O(n), Space O(n)
// Leetcode: https://leetcode.com/problems/valid-palindrome/
// Solution 1: Two Pointer Approach

function isPalindrome(s) {
    let clean=s.replace(/[^a-zA-Z0-9]/g,'').toLowerCase()
    let left=0
    let right=clean.length-1
    while(left<right){
        if(clean[left]!==clean[right]){
            return false
        }
        left++
        right--
    }
    return true
}
// Solution 2: String Reversal Approach

function isPalindromeReversal(s) {
    let clean=s.replace(/[^a-zA-Z0-9]/g,'').toLowerCase()
    let reversed=clean.split('').reverse().join('')
    return clean===reversed
}
// Test Cases
console.log(isPalindrome("A man, a plan, a canal: Panama")); // true
console.log(isPalindrome("race a car")); // false
console.log(isPalindromeReversal("A man, a plan, a canal: Panama")); // true    
console.log(isPalindromeReversal("race a car")); // false

// Best Approach: Two Pointer Approach
// Complexity Analysis: Time Complexity: O(n), Space Complexity: O(1)