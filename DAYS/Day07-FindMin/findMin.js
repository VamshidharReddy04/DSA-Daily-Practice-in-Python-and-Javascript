// Array Problem : Find Minimum in Rotated Sorted Array
// Given the array nums after the rotation and an integer target, 
// return the index of target if it is in nums, or -1 if it is not in nums.
// Example 1: Input: nums = [4,5,6,7,0,1,2], Output: 0
// Example 2: Input: nums = [3,4,5,1,2], Output: 1
// Example 3: Input: nums = [1],  Output: 1

// Leetcode Problem Link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
// Solution : Using Binary Search

function findMin(nums) {
    let left=0;
    let right=nums.length-1;
    while (left < right){
        let mid = Math.floor((left +right /2));
        if(nums[mid]>nums[right]){
            left=mid +1
        }else{
            right=mid
        }
    }return nums[left];
}
console.log(findMin([4,5,6,7,0,1,2])); // Output: 0
console.log(findMin([1])); // Output: 1
console.log(findMin([3,4,5,1,2])); // Output: 1
