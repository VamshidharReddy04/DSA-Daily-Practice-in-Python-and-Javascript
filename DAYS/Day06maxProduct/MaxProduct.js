// Array problem: Maximum Product Subarray
// https://leetcode.com/problems/maximum-product-subarray/
// Given an integer array nums, find the contiguous subarray within an array 
// (containing at least one number) which has the largest product.

// Example 1: Input: [2,3,-2,4] Output: 6
// Example 2: Input: [-2,0,-1] Output: 0
// Example 3: Input: [-2,3,-4] Output: 24

function maxProduct(nums) {
    // Initialize maxProduct, minProduct and maxOverall
    let maxProduct =nums[0];
    let minProduct = nums[0];
    let maxOverall = nums[0];

    for (let i = 1; i < nums.length; i++) {
        let num = nums[i];
        // Store the current maxProduct in temp
        let temp = maxProduct;
        // Update maxProduct
        maxProduct = Math.max(num,num*maxProduct,num *minProduct);
        // Update minProduct
        minProduct = Math.min(num,num*temp,num *minProduct);
        // Update maxOverall
        maxOverall = Math.max(maxOverall, maxProduct);
    }
    return maxOverall;
}

// Test cases
console.log(maxProduct([2,3,-2,4])); // Output: 6
console.log(maxProduct([-2,0,-1])); // Output: 0
console.log(maxProduct([-2,3,-4])); // Output: 24

// Best Approach:Optimal Approach (Kadane's Algorithm Variation)
// Complexity Analysis: Time Complexity: O(n) Space Complexity: O(1)