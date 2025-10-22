# Strings - Valid Parenthese leetcode 20
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# Example 1: Input s = "()" Output: true
# Example 2: Input s = "()[]{}" Output: true
# Example 3: Input s = "(]" Output: false
# Different Approaches:
# 1. Using Stack-Time O(n) Space O(n)
# 2. Using HashMap-Time O(n) Space O(n)
# 3. Using String Replacement-Time O(n^2) Space O(1)

# Leetcode: https://leetcode.com/problems/valid-parentheses/
# Solution:
# Using Stack and HashMap to check for valid parentheses
def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in '([{':
            stack.append(char) # Push opening brackets onto stack
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]: #check the stack
                return False
            stack.pop() 
    return not stack
# Test Cases
print(isValid("()"))          # True
print(isValid("()[]{}"))      # True
print(isValid("(]"))         # False
print(isValid("([{}])"))     # True
# Best Approach Using Stack and HashMap
# Complexity Analysis: Time Complexity: O(n) Space Complexity: O(n)