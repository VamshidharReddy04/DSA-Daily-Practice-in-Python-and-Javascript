// Array + Hashset
// Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
// Example 1: Input: nums = [100,4,200,1,3,2] Output: 4 Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
// Example 2: Input: nums = [0,3,7,2,5,8,4,6,0,1] Output: 9

//Different Approaches:
// 1.Sorting: Time: O(n log n), Space: O(1) or O(n) depending on sorting algorithm
// 2.HashSet: Time: O(n), Space: O(n)
// 3.Union-Find: Time: O(n), Space: O(n)

//Approach 2: HashSet
// LeetCode: https://leetcode.com/problems/longest-consecutive-sequence/solution/

function longestConsecutive(nums) {
    if(nums.length === 0) return 0;
    const numSet =new Set(nums);
    let longestStreak = 0;
    for (const num of numSet){
        if(!numSet.has(num-1)){ // Check if it's the start of a sequence
            let length =1; // Start a new sequence
            while(numSet.has(num+length)){ // Check for the next consecutive number
                length++; // Increment length for each consecutive number found
            }
            longestStreak = Math.max(longestStreak, length); // Update the longest streak if current length is greater
        }
    }
    return longestStreak;
}
// Test Cases:
console.log(longestConsecutive([100,4,200,1,3,2])); // Output: 4
console.log(longestConsecutive([0,3,7,2,5,8,4,6,0,1])); // Output: 9
confirm.log(longestConsecutive([])); // Output: 0

// Best Approach: HashSet
//Complexity Analysis: Time Complexity: O(n) Space Complexity: O(n)