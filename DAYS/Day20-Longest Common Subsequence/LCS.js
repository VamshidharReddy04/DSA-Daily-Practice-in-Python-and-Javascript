// Dynamic Programming : Longest Common Subsequence
//Given two strings s1 and s2, return the length of the longest common subsequence.
// Example 1: Input: s1 = "abcde", s2 = "ace" Output: 3 
// Example 2: Input: s1 = "abc", s2 = "abc" Output: 3
// Example 3: Input: s1 = "abc", s2 = "def" Output: 0

// Different Approaches
// 1. Recursion (Brute Force)
// 2. Memoization (Top-Down DP)
// 3. Tabulation (Bottom-Up DP)

//Solution 1: Borute Force (Recursion)
function LCS(s1 ,s2){
    let n = s1.length;
    let m = s2.length;
    let dp=Array.from({length:n+1},()=>Array(m+1).fill(0)); //2D Array
    for (let i=1;i<=n ;i++){    //i and j starts from 1 because 0th row and column is for empty string
        for (let j=1;j<=m ;j++){
            if (s1[i-1]===s2[j-1]){  //i-1 and j-1 because index starts from 0
                dp[i][j]=1+dp[i-1][j-1];  //if characters match, add 1 to the result of previous characters
            }else{
                dp[i][j]=Math.max(dp[i-1][j],dp[i][j-1]); //if characters don't match, take the maximum of the two possibilities
            }
        }
    }return dp[n][m];   //return the value in the bottom-right corner of the matrix
}
// Test Cases
console.log(LCS("abcde","abce")); //4
console.log(LCS("abc","ac")); //2
console.log(LCS("abc","def")); //0  
console.log(LCS("abcdgh","abedfhr")); //4
// Best Approach: Tabulation (Bottom-Up DP)
// Complexity Analysis: Time Complexity - O(n*m) , Space Complexity - O(n*m)
