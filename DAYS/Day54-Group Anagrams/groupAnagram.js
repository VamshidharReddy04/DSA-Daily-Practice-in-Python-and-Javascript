// String - Group Anagrams leetcode 49
// Given an array of strings strs, group the anagrams together. You can return the answer in any order.
// Example 1: Input: strs = ["eat","tea","tan","ate","nat","bat"] Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
// Example 2: Input: strs = [""] Output: [[""]]
// Example 3: Input: strs = ["a"] Output: [["a"]]

// Different Approaches:
// 1. Sorting approach - Time: O(NKlogK) Space: O(NK) 
// 2. Counting approach - Time: O(NK) Space: O(NK)
// Leetcode https://leetcode.com/problems/group-anagrams/solutions/3425535/javascript-sorting-and-counting-approach/
// Solution 2: Counting approach

function groupAnagrams(strs) {
    const map=new Map();
    for(const str of strs){
        const count =new Array(26).fill(0); // Count array 26 letters
        for(const char of str){
            // use charCodeAt to get ASCII code and subtract 'a' to get index 0-25
            count[char.charCodeAt(0) - 'a'.charCodeAt(0)]++ // Increment count for each character
        }
        const key=count.join('#'); // Create a unique key for the count array
        if(!map.has(key)){    
            map.set(key,[]); // If key not present, set empty array
        }
        map.get(key).push(str); //get key letter and push str
    }
    return Array.from(map.values());
}

// Test cases
console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"])); //Output [["bat"],["nat","tan"],["ate","eat","tea"]]
console.log(groupAnagrams([""])); //Output [[""]]
console.log(groupAnagrams(["a"])); //Output [["a"]]

// Best Approach: Counting approach
// Complexity Analysis: Time Complexity: O(NK) , Space Complexity: O(NK)
