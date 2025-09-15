# Array Problem 11: Container With Most Water
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.    
# Example 1: Input: [1,8,6,2,5,4,8,3,7] Output: 49
# Example 2: Input: [1,1] Output: 1
# Example 3: Input: [4,3,2,1,4] Output: 16

# Solution: Two Pointer Approach
# Leetcode: https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left ,right=0,len(height)-1 
        maxArea=0 
        while left<right: # Two pointers approach
            area=min(height[left],height[right])*(right-left) # Calculate area
            maxArea=max(maxArea,area) # Update maxArea
            if height[left]<height[right]: # Move the pointer pointing to the shorter line
                left+=1  # Move left pointer to the right
            else:
                right-=1 # Move right pointer to the left
        return maxArea

# Test Cases
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(Solution().maxArea([1,1]))                  # Output: 1
print(Solution().maxArea([4,3,2,1,4]))            # Output: 16

# Best Approach: Two Pointer Approach
# Complexity Analysis: Time Complexity: O(n) Space Complexity: O(1)
