// Binary Problem :No. of 1 Bits
// Given a number N, count the total number of 1's in its binary representation.
// Example 1: Input: 11 Output: 3
// Explanation: Binary representation of 11 is 1011 which has three 1's.
// Example 2: Input: 128 Output: 1
// Example 3: Input: 255 Output: 8

function hammingWeight(n){
   let count =0
   while (n >0){  // loop till n becomes 0
       n=n&(n-1) // & operation reduces the last set bit to 0
       count++  // increment count for every set bit
   }
   return count // return count of set bits
}

// Test Cases
console.log(hammingWeight(11)) //3
console.log(hammingWeight(128)) //1
console.log(hammingWeight(255)) //8

// Best Approach: Using Brian Kernighan’s Algorithm
// Complexity Analysis: Time Complexity: O(1) , Space Complexity: O(1)