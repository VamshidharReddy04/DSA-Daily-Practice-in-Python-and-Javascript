// Strings : Longest Repeating Character Replacement leetcode 424
// Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.
// Example 1: Input: s = "ABAB", k = 2 Output: 4
// Example 2: Input: s = "AABABBA", k = 1 Output: 4
// Example 3: Input: s = "AAAA", k = 2 Output: 4

// Different Approach
// 1. Brute Force :Time O(N^2) Space O(1)
// 2. Sliding Window : Time O(N) Space O(1)

// Solution 2 : Sliding Window
// Leetcode :https://leetcode.com/problems/longest-repeating-character-replacement/description/

function characterReplacement(s, k) {
    let left=0, maxLength=0, maxCount=0;
    const count=new Map();

    for(right=0;right<s.length;right++){
        char=s[right];
        count.set(char,(count.get(char)||0)+1);
        maxCount=Math.max(maxCount,count.get(char));
    }
    while((right-left+1)-maxCount>k){
        count.set(s[left],count.get(s[left])-1);
        left++;
    }
    return Math.max(maxLength,right-left+1);
}

// Test Cases
console.log(characterReplacement("ABAB", 2)); // Output: 4
console.log(characterReplacement("AABABBA", 2)); // Output: 6
console.log(characterReplacement("AAAA", 2)); // Output: 4