# what if the array is sorted? we can use binary search to find the two numbers
# Given an Array of Integers nums and an Integer target,return indices of the two numbers such that they add up to target.

# Sorted Array allows us to use the two-pointer technique to find the two numbers that add up to the target.


def twoSumSorted(nums, target):
    left ,right=0,len(nums)-1 # initialize two pointers
    while left<right:
        sum=nums[left]+nums[right] # calculate the sum of the two numbers
        if sum==target: # if the sum is equal to the target
            return[left,right] # return the indices
        
        elif sum<target: # if the sum is less than the target
            left+=1 # move the left pointer to the right
            
        else:
            right-=1 # move the right pointer to the left
    return[] # if no solution is found, return an empty array

# Test cases
print(twoSumSorted([2,7,11,15],9))
# output: [0,1]
print(twoSumSorted([3,2,4],6))
# output: []
print(twoSumSorted([3,3],6))
# output: [0,1]

# Approach: Two Pointer
# Time Complexity: O(n)
# Space Complexity: O(1)