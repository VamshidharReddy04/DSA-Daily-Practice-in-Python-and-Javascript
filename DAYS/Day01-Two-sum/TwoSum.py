# Given an Array of Integers nums and an Integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.


# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

def twoSums(nums,target):
    seen ={}
    for i ,nums in enumerate(nums):
        result =target-nums
        if result in seen:
            return[seen[result],i]
        seen[nums]=i
print(twoSums([2,7,11,15],9))
# output: [0,1]
print(twoSums([3,2,4],6))
# output: [1,2]
print(twoSums([3,3],6))
# output: [0,1]

# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the number of elements in the input array.
# The function uses a hash map to store the numbers and their indices as it iterates through the array.
# The space complexity is also O(n) in the worst case, where all elements are stored in the hash map.
# The function iterates through the array once, performing constant-time operations for each element.
