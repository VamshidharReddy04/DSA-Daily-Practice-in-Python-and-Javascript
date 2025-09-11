# Array Product Except Self
# given an integer array nums, return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i].

# Approach: Prefix and Suffix Product
class soultion:

    def productExceptSelf(self,nums):
        n=len(nums)
        res=[1]*n
        prefix=1  # prefix is the product of all the elements to the left of the current index
        for i in range(n):
            res[i]*=prefix
            prefix *=nums[i]
        suffix=1  # suffix is the product of all the elements to the right of the current index
        for i in range(n-1,-1,-1):
            res[i]*=suffix
            suffix*=nums[i]
        return res

# test cases
print(soultion().productExceptSelf([1,2,3,4]))
# output: [24,12,8,6]
print(soultion().productExceptSelf([-1,1,0,-3,3]))
# output: [0,0,9,0,0]

# Complexity Analysis:
# Brute Force Approach: Time Complexity: O(n^2) , Space Complexity: O(1)
# Prefix and Suffix Product: Time Complexity: O(n), Space Complexity: O(n)