// Dynamic Progrmamming : Longest Increasing Subsequence
// Problem Statement: Given an integer array nums, return the length of the longest strictly increasing subsequence.
// A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
// Example 1: Input: nums = [10,9,2,5,3,7,101,18] Output: 4
// Example 2: Input: nums = [0,1,0,3,2,3] Output: 4
// Example 3: Input: nums = [7,7,7,7,7,7,7] Output: 1

// Approaches:
// 1. Recursion (Brute Force)
// 2. Memoization (Top-Down DP)
// 3. Tabulation (Bottom-Up DP)
// 4. Space Optimization (Optimized Bottom-Up DP)
// 5. Binary Search

// Soultion 5 : Binary Search
// LeetCode: https://leetcode.com/problems/longest-increasing-subsequence/description/

function lengthOfLIS(nums){
    let sub=[];      // sub array to store the longest increasing subsequence
    for (let num of nums){ 
        if(sub.length===0 || num>sub[sub.length-1]){  // if sub is empty or num is greater than the last element of sub
            sub.push(num);  // if num is greater than the last element of sub, push it to sub
        }else{
            let left =0,right=sub.length-1
            while(left<right){
                let mid =Math.floor((left+right)/2); // find the mid index
                if(sub[mid ]<num){  // if mid element is less than num, search in the right half
                    left = mid +1;  // move left to mid +1
                }else{
                    right = mid;   // move right to mid
                }
            }
            sub[left]=num;  // replace the element at left index with num
        }
    }    
    return sub.length  // return the length of sub array
}
// Test Cases:
console.log(lengthOfLIS([10,9,2,5,3,7,101,18]))  // Output: 4
console.log(lengthOfLIS([0,1,0,3,2,3]))  // Output: 4
console.log(lengthOfLIS([7,7,7,7,7,7,7]))  // Output: 1

// Best Approach : Binary Search
// Complexity Analysis: Time Complexity: O(n log n) ,Space Complexity: O(n) (for sub array)
