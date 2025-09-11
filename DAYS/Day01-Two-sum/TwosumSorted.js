//  what if the array is sorted? we can use binary search to find the two numbers
//  Given an Array of Integers nums and an Integer target,return indices of the two numbers such that they add up to target.

//  Sorted Array allows us to use the two-pointer technique to find the two numbers that add up to the target.


function TwoSumSorted(nums, target) {
    // Initialize two pointers
    let left=0;
    let right=nums.length-1;

    // Loop until the two pointers meet
    while(left<right){
        let sum=nums[left]+nums[right]
        // If the sum is equal to the target, return the indices
        if(sum===target){
            return [left,right];
        }
        // If the sum is less than the target, move the left pointer to the right
        else if(sum<target){
            left++;
        }
        // If the sum is greater than the target, move the right pointer to the left
        else{
            right--;
        }
    }
    // If no solution is found, return an empty array
    return[];
}


console.log(TwoSumSorted([2,7,11,15],9));
// output: [0,1]
console.log(TwoSumSorted([3,2,4],6));
// output: []
console.log(TwoSumSorted([3,3],6));
// output: [0,1]

// approach: two-pointer
// Time Complexity: O(n) where n is the number of elements in the array.
// Space Complexity: O(1)