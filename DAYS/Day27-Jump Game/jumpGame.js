// Greedy + Dynamic Programming : Jump Game
// Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
// Example 1: Input: nums = [2,3,1,1,4] Output: true
// Example 2: Input: nums = [3,2,1,0,4] Output: false

// Different Approaches:
// 1. Greedy Approach - Time O(n) Space O(1)
// 2. Dynamic Programming Approach - Time O(n^2) Space O(n)

// Solution 1: Greedy Approach
function canJump(nums) {
    let maxReach =0;           // max reachable index
    for(let i=0; i<nums.length; i++){
        if(i > maxReach) return false;  // if current index is greater than max reachable index, return false
        maxReach =Math.max(maxReach,i+nums[i]) // update max reachable index
    }
    return true;  // if we reach here, it means we can reach the last index
}
// Test Cases
console.log(canJump([2,3,1,1,4])); // true
console.log(canJump([3,2,1,0,4])); // false

// Best Approach: Greedy Approach
// Complxity Anaysis: Time O(n) Space O(1)