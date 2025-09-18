// Dynamic Programming:Robber House Problem (Cricular)
// Given n houses in a circle, each house has a certain amount of money stashed.
// All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
// Robber has to rob all the houses with the maximum amount of money.//
// Example 1: Input: nums = [2,3,2] Output: 3
// Example 2: Input: nums = [1,2,3,1] Output: 4
// Example 3: Input: nums = [0] Output: 0

// Different Approach:
// 1. Recursion (Brute Force)
// 2. Recursion + Memoization (Top Down)
// 3. Tabulation (Bottom Up)
// 4. Space Optimization
// 5. Circular House Robber

// Approach 4: Space Optimization
function rob(nums) {
    const n = nums.length;
    if (n === 0) return 0;
    if (n === 1) return nums[0];
    function robLinear(arr) {
        let prev1 = 0, prev2 = 0;
        for (let num of arr) {
            let curr = Math.max(num + prev2, prev1);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
    // Exclude first or last house
    return Math.max(robLinear(nums.slice(0, n - 1)), robLinear(nums.slice(1)));
}
// Test cases
console.log(rob([2, 3, 2])); // 3
console.log(rob([1, 2, 3, 1])); // 4
console.log(rob([0])); // 0
// Best Approach : Circular House Robber
// Complexity Analysis : Time O(n) | Space O(1)