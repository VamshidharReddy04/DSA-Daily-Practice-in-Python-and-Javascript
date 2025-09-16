// Binary Problem : Missing Number
//Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
// Example 1: Input: nums = [3,0,1] Output: 2
// Example 2: Input: nums = [0,1] Output: 2
// Example 3: Input: nums = [9,6,4,2,3,5,7,0,1] Output: 8

// Soultion 1: Using Gauss's Formula 
// Soultion 2: Using XOR operation
// Leetcode Link: https://leetcode.com/problems/missing-number/

// Solution 1: Using Gauss's Formula
function missingNumber(nums) {
    let n=nums.length ; // Since one number is missing, the length of the array is n
    let total=n*(n+1)/2; // Gauss's Formula
    let actual=nums.reduce((a,b)=>a+b,0) // Sum of all elements in the array
    return total-actual; // Missing Number
}
// Test Cases
console.log(missingNumber([3,0,1])) //2
console.log(missingNumber([0,1])) //2
console.log(missingNumber([9,6,4,2,3,5,7,0,1])) //8

// Solution 2: Using XOR operation
function missingNumberXOR(nums) {
    let n=nums.length; // Since one number is missing, the length of the array is n
    let xorAll=0;      // XOR of all numbers from 0 to n
    for(let i=0;i<=n;i++){ // Loop from 0 to n
        xorAll ^=i;    // XOR operation
    }
    for(let num of nums){  // Loop through the array
        xorAll ^=num;  // XOR operation with all elements in the array
    }
    return xorAll; // Missing Number
}

// Test Cases
console.log(missingNumberXOR([3,0,1])) //2
console.log(missingNumberXOR([0,1])) //2
console.log(missingNumberXOR([9,6,4,2,3,5,7,0,1])) //8

// Best Approach:1.Guass's Formula , 2.XOR operation
// Complexity Analysis: Time Complexity: O(n) , Space Complexity: O(1)
