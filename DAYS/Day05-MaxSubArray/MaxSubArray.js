// Array problem: Maximum Subarray
// Given an integer array nums, find the contiguous subarray 
// (containing at least one number) which has the largest sum and return its sum.


function maxSubArray(nums){
    let maxSum=nums[0]; // Initialize maximum sum to the first element of the array
    let curSum=0; // Initialize current sum to 0
 
    for(let num of nums){
        curSum += num // Add the current element to the current sum
        maxSum=Math.max(maxSum,curSum); // Update the maximum sum if the current sum is greater
        if (curSum<0){ // If the current sum is negative, reset it to 0
            curSum = 0;
        }
    }
    return maxSum; // Return the maximum subarray sum
}

// Test cases
console.log(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
// output: 6
console.log(maxSubArray([1]))
// output: 1
console.log(maxSubArray([5,4,-1,7,8]))
// output: 23
console.log(maxSubArray([-1]))
// output: -1

// Best Approach: Kadane's Algorithm
// complexity Analysis : Time complexity: O(n) ,Space complexity: O(1)
