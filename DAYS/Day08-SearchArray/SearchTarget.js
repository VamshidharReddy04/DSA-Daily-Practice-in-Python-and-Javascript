// Array Problem: Search in Rotated Sorted Array
// Given the array nums after the rotation and an integer target,
// return the index of target if it is in nums, or -1 if it is not in nums.
// You must write an algorithm with O(log n) runtime complexity.
// Example 1: Input: nums = [4,5,6,7,0,1,2], target = 0 Output: 4
// Example 2: Input: nums = [4,5,6,7,0,1,2], target = 3 Output: -1
// Example 3: Input: nums = [1], target = 0 Output: -1

// Solution Binary Search
// leetcode link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

function search(nums, target) {
  let left = 0;
  let right = nums.length - 1;
  // loop until left pointer is greater than right pointer
  while (left <= right) {
    // calculate mid index
    let mid = Math.floor((left + right) / 2);
    // if mid element is equal to target, return mid index
    if (nums[mid] === target) return mid;
    // if left half is sorted
    if (nums[left] <= nums[mid]) {
      // if target is in left half, search in left half
      if (target >= nums[left] && target < nums[mid]) {
        right = mid - 1;
      }
      // else search in right half
      else {
        left = mid + 1;
      }
    }
    // if right half is sorted
    // if target is in right half, search in right half
    else {
      if (target > nums[mid] && target <= nums[right]) {
        left = mid + 1;
      }
      // else search in left half
      else {
        right = mid - 1;
      }
    }
  }
  // if target is not found, return -1
  return -1;
}

// Test Cases
console.log(search([4, 5, 6, 7, 0, 1, 2], 0)); // Output: 4
console.log(search([4, 5, 6, 7, 0, 1, 2], 3)); // Output: -1
console.log(search([1], 0)); // Output: -1

// Best Approach: Binary Search
// Complexity Analysis : Time Complexity: O(log n) , Space Complexity: O(1)
