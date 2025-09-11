// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// Example:
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]

function TwoSum(nums, target) {
    const  seen={};
    for (let i=0;i<nums.length;i++){
        let result=target-nums[i];
        if(result in seen){
            return[seen[result],i];
        }
        seen[nums[i]]=i;
    }
}
console.log(TwoSum([2,7,11,15],9));
// output: [0,1]
console.log(TwoSum([3,2,4],6));
// output: [1,2]
console.log(TwoSum([3,3],6));
// output: [0,1]

// Time Complexity: O(n) where n is the number of elements in the array.
// Space Complexity: O(n)
