//Binary Problem : Counting Bits
//Given an integer n, return an array ans where ans[i] is the 
// number of 1's in the binary representation of the integer i.

// Soultion : Optimized Dynamic Programming

function countBits(n){
    let dp=new Array(n+1).fill(0)
    for (let i=1;i<=n ;i++){
        dp[i]=dp[i >> 1]+(i&1)
    }
    return dp
}
// Test Cases
console.log(countBits(5)) //Output : [0,1,1,2,1,2]
console.log(countBits(2)) //Output : [0,1,1]

// Best Approach : Optimized Dynamic Programming
// Complexity Analysis : Time : O(n), Space : O(1)
