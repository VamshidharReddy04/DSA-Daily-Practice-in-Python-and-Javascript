# Given an Array of Integers nums and an Integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

def twoSums(nums, target):
    # create a hash map to store the elements and their indices
    seen = {}
    for i, num in enumerate(nums):
        # calculate the result of the current element and the target
        result = target - num
        # if the result is in the hash map, return the indices
        if result in seen:
            return [seen[result], i] # store the current element in the hash map
        seen[num] = i
    # if no solution is found, return an empty array
    return []

# Test cases
print(twoSums([2,7,11,15],9))
# output: [0,1]
print(twoSums([3,2,4],6))
# output: [1,2]
print(twoSums([3,3],6))
# output: [0,1]

# Approach: Hash 
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)