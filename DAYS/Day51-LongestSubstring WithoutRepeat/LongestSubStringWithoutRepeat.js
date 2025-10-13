// Strings : Longest Substring Without Repeating Characters leetcode 3
// Given a string s, find the length of the longest substring without repeating characters.

// Example 1: Input: s = "abcabcbb" Output: 3
// Example 2: Input: s = "bbbbb" Output: 1 
// Example 3: Input: s = "pwwkew" Output: 3

// Different Approaches :
// 1. Brute Force Approach : O(n^3) time complexity
// 2. Sliding Window Approach : O(2n) time complexity
// Solution : Sliding Window Approach

function LongestSubstring(s){
    let left=0;
    let maxLength=0;
    const seen=new Map();

    for(let right=0;right<s.length;right++){
        const char=s[right];
        if(seen.has(char)&&seen.get(char)>=left){
            left=Math.max(left,seen.get(char)+1);
        }
        seen.set(char,right);
        maxLength=Math.max(maxLength,right-left+1);
    }
    return maxLength;
}
// Test Cases
console.log(LongestSubstring("abcabcbb")); // Output: 3
console.log(LongestSubstring("bbbbb"));    // Output: 1
console.log(LongestSubstring("pwwkew"));   // Output: 3

// Best Approach : Sliding Window Approach 
// Complexity Analysis: Time complexity : O(n), Space complexity : O(n) 