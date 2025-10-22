// Strings - Valid Parentheses leetcode 20
// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
// Example 1: Input s = "()" Output: true
// Example 2: Input s = "()[]{}" Output: true
// Example 3: Input s = "(]" Output: false
// Different Approaches: 
// 1. Stack - Time Complexity: O(n), Space Complexity: O(n)
// 2. HashMap - Time Complexity: O(n), Space Complexity: O(n)
// 3. String Replacement - Time Complexity: O(n^2), Space Complexity: O(1)

// Leetcode: https://leetcode.com/problems/valid-parentheses/
// Solution:

function isValid(s) {
    const stack = [];
    const map ={')': '(', '}': '{', ']': '['};
    for (let ch of s){
      if(ch=='(' || ch=='{' || ch=='['){
        stack.push(ch);
      } else {
        if(!stack.length || stack.pop() !== map[ch]) {
          return false;
        }
      }
    }
    return stack.length === 0;
}
// Test Cases
console.log(isValid("()")); // true
console.log(isValid("()[]{}")); // true
console.log(isValid("(]")); // false
console.log(isValid("([)]")); // false

// Best Approach: Stack
// Complexity Analysis: Time Complexity: O(n), Space Complexity: O(n)