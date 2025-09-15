// Array Problem: Three Sum 
// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
// Notice that the solution set must not contain duplicate triplets.                                        
// Example 1: Input: nums = [-1,0,1,2,-1,-4] Output: [[-1,-1,2],[-1,0,1]]
// Example 2: Input: nums = [1,0,1] Output: []
// Example 3: Input: nums = [0,0,0] Output: [[0,0,0]]

// Optimized Two Pointer Approach
function threeSum(nums) {
    nums.sort((a,b)=>a-b); // Sort the array to use two-pointer technique
    const result = [];
    const n = nums.length;
    for (let i = 0; i < n - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue; // Skip duplicates for the first element
        let left = i + 1;
        let right = n - 1;
        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];
            if (sum === 0) {
                result.push([nums[i], nums[left], nums[right]]);
                while (left < right && nums[left] === nums[left + 1]) left++; // Skip duplicates for the second element
                while (left < right && nums[right] === nums[right - 1]) right--; // Skip duplicates for the third element
                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }        
        }
    }
    return result;
}

// Test Cases
console.log(threeSum([-1,0,1,2,-1,-4]));  // Output: [[-1,-1,2],[-1,0,1]]
console.log(threeSum([1,0,1])); // Output: []
console.log(threeSum([0,0,0])); // Output: [[0,0,0]]

// Best Approach : Optimized Two Pointer Approach
// Complexity Analysis: Time complexity: O(n^2) , Space complexity: O(1)