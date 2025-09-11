# what if the array is sorted? we can use binary search to find the two numbers
# Given an Array of Integers nums and an Integer target,return indices of the two numbers such that they add up to target.

# Sorted Array allows us to use the two-pointer technique to find the two numbers that add up to the target.

def twoSumSorted(nums, target):
    left ,right=0,len(nums)-1
    while left<right:
        sum=nums[left]+nums[right]
        if sum==target:
            return[left,right]
        elif sum<target:
            left+=1
        else:
            right-=1
    return[]
print(twoSumSorted([2,7,11,15],9))
# output: [0,1]
print(twoSumSorted([3,2,4],6))
# output: []
print(twoSumSorted([3,3],6))
# output: [0,1]

# Time Complexity: O(n)
# Space Complexity: O(1)