// Binary Problem: Single Number
// Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
//Example 1:Input: nums = [2,2,1] Output: 1
//Example 2:Input: nums = [4,1,2,1,2] Output: 4
//Example 3:Input: nums = [1] Output: 1

function singleNumber(nums) {
    let result =0
    for (let num of nums) { 
        result ^= num // XOR operation
    }
    return result // The single number will remain after all pairs cancel out
}
// Test cases
console.log(singleNumber([4,1,2,1,2])) // Output: 4
console.log(singleNumber([2,2,1])) // Output: 1
console.log(singleNumber([1])) // Output: 1

//Approach: Using XOR operation
//Complexity Analysis: Time complexity: O(n), Space complexity: O(1)