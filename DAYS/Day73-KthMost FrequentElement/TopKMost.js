// Heap : K most Frequent Elements (LeetCode 347)
// Given a non-empty array of integers, return the k most frequent elements.
// Example 1: Input: nums = [1,1,1,2,2,3], k = 2 Output: [1,2]
// Example 2: Input: nums = [1], k = 1 Output: [1]

// Different Approaches:
// 1. Using HashMap and Sorting - Time O(N log N), Space O(N)
// 2. Using HashMap and Min-Heap (Priority Queue) - Time O(N log K), Space O(N)
// 3. Using Bucket Sort - Time O(N), Space O(N)
// leetcode link: https://leetcode.com/problems/top-k-frequent-elements/
// Solution:

function topKFrequent(nums, k) {
    const freq=new Map();
    for(let num of nums){
        freq.set(num,(freq.get(num)||0)+1);  // Count frequency of each number
    }
    const bucket=Array(nums.length+1).fill().map(()=>[]); // Create buckets for frequencies
    for(let[num,count]of freq){
        bucket[count].push(num); 
    }
    const res=[]; // Result array
    for(let i=bucket.length-1;i>=0&&res.length<k;i--){ // Traverse buckets from high to low frequency
        for(let num of bucket[i]){
            res.push(num);  // Add number to result
            if(res.length===k) return res;  // Return result when we have k elements
        }
    }
}

// Test Cases
console.log(topKFrequent([1,1,1,2,2,3], 2)); // Output: [1,2]
console.log(topKFrequent([1], 1)); // Output: [1]
console.log(topKFrequent([4,1,-1,2,-1,2,3], 2)); // Output: [-1,2]

// Complexity Analysis: Time Complexity: O(N), Space Complexity: O(N)
