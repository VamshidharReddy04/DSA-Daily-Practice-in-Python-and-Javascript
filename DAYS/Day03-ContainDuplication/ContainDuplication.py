# Array problem Given an integer array, find if the array contains any duplicates. 
# Your function should return true if any value appears at least twice in the array, and 
# it should return false if every element is distinct.

# Example 1:
# Input: [1,2,3,1]
# Output: true
# Example 2:
# Input: [1,2,3,4]
# Output: false
# Example 3:
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution:
    def conatainsDuplication(self,nums):
        seen = set()
        # loop through the array to check for duplicates
        seen= set()
        for num in nums:
            if num in seen:
                # if a duplicate is found, return True
                return True
            seen.add(num)
        # if no duplicates are found, return False
        return False

# Test Case
print(Solution().conatainsDuplication([1,2,3,1])) # True
print(Solution().conatainsDuplication([1,2,3,4])) # False
print(Solution().conatainsDuplication([1,1,1,3,3,4,3,2,4,2])) # True

# Approach : Hashing
# Time Complexity: O(n)
# Space Complexity: O(n)

