// Dynamic Programming: Rob the House
// Given an interger array nums representing the amount of money of each house, 
// return the maximum amount of money you can rob tonight without alerting the police (i.e., without robbing two adjacent houses).
// Example 1: Input: nums = [1,2,3,1] Output: 4 Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4.
// Example 2: Input: nums = [2,7,9,3,1] Output: 12 Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1). Total amount you can rob = 2 + 9 + 1 = 12.

// Different Approaches: 
// 1. Recursive Approach    
// 2. Memoization Approach
// 3. Tabulation Approach   
// 4. Space Optimization Approach

// Solution 4: Space Optimization Approach
function rob(nums){
    let rob1 =0 ;
    let rob2 =0;
    for(let n of nums){
        let temp = Math.max(n + rob1, rob2);
        rob1 = rob2;
        rob2 = temp;
    }
    return rob2;
}
// Test Cases
console.log(rob([1,2,3,1])); // Output: 4
console.log(rob([2,7,9,3,1])); // Output: 12
console.log(rob([2,1,1,2])); // Output: 4
