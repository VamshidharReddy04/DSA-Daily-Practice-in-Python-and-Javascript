// Binary Problem - Sum Two Numbers
// Problem Statement: Given two integers a and b, return the sum of the two integers without using the operators + and -.
// Example 1: input: a = 1, b = 2; output:3
// Example 2: input: a = -2, b = 3; output:1
// Example 3: input: a = 2, b = 3; output: 5
// Approach: Bit Manipulation , using XOR and AND operations
// XOR operation gives sum without carry and AND operation gives carry bits.
// We repeat this process until there is no carry left.

function getSum(a,b){
    while(b !==0){
        let sum =a^b // sum without carry
        let carry = (a&b)<<1 // carry bits
        a = sum     // update a to sum
        b = carry   // update b to carry
    }
    return a   // return sum
}
// Test cases
console.log(getSum(1,2)) // Output: 3
console.log(getSum(-2,3)) // Output: 1
console.log(getSum(2,3)) // Output: 5

// Best Approach : Bit Manipulation
// Complexity Analysis: Time Complexity: O(1). Space Complexity: O(1).