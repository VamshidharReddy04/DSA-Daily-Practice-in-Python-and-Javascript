// Dynamic Programming : Word Break Problem
// Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
// Note that the same word in the dictionary may be reused multiple times in the segmentation.
// Example 1: Input: s = "leetcode", wordDict = ["leet","code"] Output: true Explanation: Return true because "leetcode" can be segmented as "leet code".
// Example 2: Input: s = "applepenapple", wordDict = ["apple","pen"] Output: true Explanation: Return true because "applepenapple" can be segmented as "apple pen apple". Note that you are allowed to reuse a dictionary word.
// Example 3: Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] Output: false
// Different Approaches :
// 1. Recursion with Memoization (Top-Down DP)
// 2. Dynamic Programming (Bottom-Up DP) - Best Approach

// Solution 2 : Dynamic Programming (Bottom-Up DP)
function wordBreak(s,wordDict){
    let wordSet = new Set(wordDict);
    let n=s.length;
    let dp = new Array(n+1).fill(false);
    dp[0]=true; // Empty string can be segmented
    for(let i=1;i<=n;i++){  // Check all prefixes
        for(let j=0;j<i;j++){ // Check all possible partitions
            if(dp[j] && wordSet.has(s.substring(j,i))){  
                dp[i]=true;  // If partition is possible
                break;
            }
        }
    }
    return dp[n];
}
// Test Cases
console.log(wordBreak("leetcode", ["leet", "code"]));  // Output: true
console.log(wordBreak("applepenapple", ["apple", "pen"]));  // Output: true
console.log(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]));  // Output: false

// Best Approach : Dynamic Programming (Bottom-Up DP)
// Complexity Analysis: Time Complexity: O(n^2) , Space Complexity: O(n) 

