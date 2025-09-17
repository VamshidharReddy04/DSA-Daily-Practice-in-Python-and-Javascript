# Dynamic Programming : Climbing Stairs
# Given a staircase with n steps, you can climb either 1 step or 2 steps at a time.
# Write a function to count the number of distinct ways to reach the top of the staircase.
# Example 1: Input: n = 2 Output: 2
# Example 2: Input: n = 3 Output: 3
# Example 3: Input: n = 45 Output: 1836311903
# Approach 1 : Recursion  
# Approach 2 : Memoization (Top-Down Approach)
# Approach 4 : Fibonacci Number

# Approach 3 : Tabulation (Buttom-Up Approach)
# Solution : Optimized DP (Buttom-Up Approach)
# Leetcode : https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    def climbStairs(self,n):
        if n==1 or n==2: # n=1 or n=2 are base cases
            return n 
        a,b=1,2 # a=ways to reach step 1, b=ways to reach step 2
        for i in range(3,n+1): # Calculate ways to reach step i
            a,b=b,a+b # Update a and b for next step
        return b # b now contains ways to reach step n
# Test case 
print(Solution().climbStairs(1)) # Output: 1
print(Solution().climbStairs(2)) # Output: 2
print(Solution().climbStairs(3)) # Output: 3
print(Solution().climbStairs(45)) # Output: 1836311903

# Best Approach : Bottom-Up DP 
# Complexity Analysis: Time complexity : O(n). Space complexity : O(1).

# Approach 1: Recursion
# class Solution:
#     def climbStairs(self,n):
#         if n<=2: 
#             return n  
#         return self.climbStairs(n-1)+self.climbStairs(n-2) # Recursive call
# # Test case
# print(Solution().climbStairs(2)) # Output: 2
# print(Solution().climbStairs(3)) # Output: 3
# print(Solution().climbStairs(45)) # Output: 1836311903
# Complexity Analysis: Time complexity : O(2^n). Space complexity : O(n).

# Approach 2: Memoization (Top-Down Approach)
# class Solution:
#     def __init__(self):
#         self.memo = {} # Dictionary to store computed results
#     def climbStairs(self,n):
#         if n in self.memo:
#             return self.memo[n] # Return cached result
#         if n<=2:
#             return n
#         self.memo[n] = self.climbStairs(n-1)+self.climb
#         return self.memo[n] # Store result in memo
# # Test case
# print(Solution().climbStairs(2)) # Output: 2
# print(Solution().climbStairs(3)) # Output: 3  
# print(Solution().climbStairs(45)) # Output: 1836311903
# Complexity Analysis: Time complexity : O(n). Space complexity : O(n).

# Approach 4: Fibonacci Number
# class Solution:   
#     def climbStairs(self,n):
#         sqrt5 = 5**0.5
#         fibn = ((1+sqrt5)**(n+1)-(1-sqrt5)**(n+1))/(2**(n+1)*sqrt5)
#         return round(fibn) # Round to nearest integer
# # Test case
# print(Solution().climbStairs(2)) # Output: 2
# print(Solution().climbStairs(3)) # Output: 3
# print(Solution().climbStairs(45)) # Output: 1836311903
# Complexity Analysis: Time complexity : O(1). Space complexity : O(1).