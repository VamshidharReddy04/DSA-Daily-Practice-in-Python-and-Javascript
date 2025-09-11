// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// Example:
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]

function TwoSum(nums, target) {
    // create a hash map to store the elements and their indices
    const  seen={};
    // iterate through the array
    for (let i=0;i<nums.length;i++){
        // calculate the result of the current element and the target
        let result=target-nums[i];
        // if the result is in the hash map, return the indices
        if(result in seen){
            return[seen[result],i];
        }
        // store the current element in the hash map
        seen[nums[i]]=i;
    }
}

console.log(TwoSum([2,7,11,15],9));
// output: [0,1]
console.log(TwoSum([3,2,4],6));
// output: [1,2]
console.log(TwoSum([3,3],6));
// output: [0,1]

// Approach: Hash Map
// Time Complexity: O(n) where n is the number of elements in the array.
// Space Complexity: O(n)
