// String - Valid Anagram leetcode 242
// Given two strings s and t, return true if t is an anagram of s, and false otherwise.
//Example 1: Input: s = "anagram", t = "nagaram" Output: true
//Example 2: Input: s = "rat", t = "car" Output: false

// Different Approaches:
// Approach 1: Sorting - Time Complexity: O(n log n) , Space Complexity: O(1)
// Approach 2: Frequency Counter - Time Complexity: O(n), Space Complexity: O(1)
// Approach 3: Using HashMap - Time Complexity: O(n), Space Complexity: O(n)
// Leetcode :https://leetcode.com/problems/valid-anagram/

// Sorting Approach
function isAnagramSorting(s, t) {
    if (s.length !== t.length) return false;
    const sortedS = s.split('').sort().join('');
    const sortedT = t.split('').sort().join('');
    return sortedS === sortedT;
}
// Frequency Counter Approach
function isAnagramFrequencyCounter(s, t) {
    if (s.length !== t.length) return false;
    const frequency = {};
    for (let char of s) {
        frequency[char] = (frequency[char] || 0) + 1;
    }
    for (let char of t) {
        if (!frequency[char]) return false;
        frequency[char]--;
    }
    return true;
}

// HashMap Approach
function isAnagramHashMap(s, t) {
    if (s.length !== t.length) return false;
    const charCount = new Map();
    for (let char of s) {
        charCount.set(char, (charCount.get(char) || 0) + 1);
    }
    for (let char of t) {
        if (!charCount.has(char) || charCount.get(char) === 0) return false;
        charCount.set(char, charCount.get(char) - 1);
    }
    return true;
}

// Example usage:
console.log(isAnagramSorting("anagram", "nagaram")); // true
console.log(isAnagramFrequencyCounter("rat", "car")); // false
console.log(isAnagramHashMap("listen", "silent")); // true

// Best Approach: Frequency Counter 
// Complexity Analysis: Time Complexity: O(n), Space Complexity: O(1)