// Array problem - Product of Array Except Self
// Given an integer array nums, return an array answer such that answer[i]
//  is equal to the product of all the elements of nums except nums[i].

function productExceptSelf(nums) {
    const n=nums.length;
    const res=new Array(n).fill(1)
    let prefix=1 // prefix[i] stores the product of numbers from 0 to i-1
    for (let i=0;i<n;i++){
        res[i] *= prefix // res[i] is the product of numbers before nums[i]
        prefix *= nums[i]
    }
    let suffix=1 // suffix[i] stores the product of numbers from i+1 to n-1
    for(let i=n-1;i>=0;i--){
        res[i] *=suffix // res[i] is the product of all numbers except nums[i]
        suffix *=nums[i]
    }
    return res
}
// Test cases
console.log(productExceptSelf([1,2,3,4])) // [24,12,8,6]
console.log(productExceptSelf([-1,1,0,-3,3])) // [-0,0,9,-0,0]

// complexity analysis :
// time complexity : O(n)
// space complexity : O(n)