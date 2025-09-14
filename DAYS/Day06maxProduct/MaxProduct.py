# Array Problem: Max Product 
# Given an array of integers, find the maximum product of two integers in the array.

# Example:
# Input: [2,3,-2,4]  output: 6
# Input: [-2,0,-1]   output: 0
# Input: [-2,3,-4]   output: 24

class solution:
    def maxProduct(self,nums):
        maxProd = minProd = maxoverall = nums[0]
        maxProd=minProd=maxoverall=nums[0]
        for num in nums[1: ]:
            temp = maxProd
            # Update maxProd to be the maximum of the current number
            maxProd = max(num, num*maxProd, num*minProd)
            # Update minProd to be the minimum of the current number
            minProd = min(num, num*temp, num*minProd)
            # Update maxoverall to be the maximum of the current maxoverall and the current maxProd
            maxoverall = max(maxoverall, maxProd)
        return maxoverall
# test cases
print(solution().maxProduct([2,3,-2,4]))  # Output: 6
print(solution().maxProduct([-2,0,-1]))   # Output: 0
print(solution().maxProduct([-2,3,-4]))   # Output: 24

# Best Approach:Optimal Approach (Kadane's Algorithm Variation)
# Complexity Analysis: time complexity: O(n)  space complexity: O(1)