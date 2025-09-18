// Backtracking : Combination Sum
// Given an array of distinct integers candidates and a target integer target,
// return a list of all unique combinations of candidates where the chosen numbers sum to target.

// Example 1:Input: candidates = [2,3,6,7], target = 7 Output: [[2,2,3],[7]]
// Example 2:Input: candidates = [2,3,5], target = 8 Output: [[2,2,2,2],[2,3,3],[3,5]]
// Example 3:Input: candidates = [2], target = 1 Output: []

// Different Approach : 
// 1. Backtracking
// 2. Recursion (Brute Force)

function combinationSum(candidates,target){
    let result=[];
    function backtrack(start,target,path,sum){
        if (target === 0){
            result.push([...path]);
            return;
        }
        for(let i=start;i<candidates.length;i++){
            if(candidates[i]<=target){
                path.push(candidates[i]);
                backtrack(i,target-candidates[i],path,sum+candidates[i]);
                path.pop();
            }
        }
    }backtrack(0,target,[],0);
    return result;
}
// Test Cases
console.log(combinationSum([2,3,6,7],7)); // [[2,2,3],[7]]
console.log(combinationSum([2,3,5],8)); // [[2,2,2,2],[2,3,3],[3,5]]
console.log(combinationSum([2],1)); // []

// Best Approach : Backtrack
// Complexity Analysis : Time - O(n^target), Space - O(target)