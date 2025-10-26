// strings - Encode and Decode Strings (leetcode 271) 
// Given a string, implement an algorithm to encode it and decode it.
// Example 1: Input: "Hello" Output: "5#Hello" 
// Example 2: Input: "Hello#World" Output: "11#Hello#World"
// Different Approaches:
// 1. Join delimiter - Time O(n), Space O(n)
// 2. Length delimiter - Time O(n), Space O(n)
// Leetcode :
// Solution :
 
function encode(strs) {
    return strs.map(s=>s.length+'#'+s).join('') // Join length and string with '#' delimiter
};

function decode(s){
    let res=[],i=0; // Initialize result array and index
    while(i<s.length){
        let j=i; // Find the position of the delimiter '#'
        while(s[j]!=='#')
            j++;
        let length=parseInt(s.slice(i,j));  // Extract the length
        res.push(s.slice(j+1,j+1+length)); // Extract the string segment
        i=j+1+length;  // Move to the next segment
    }
return res;
}
// Test Cases :
console.log(encode(["Hello","World"])); // "5#Hello5#World"
console.log(decode("5#Hello5#World")); // ["Hello","World"]
console.log(encode(["Hello#World"])); // "11#Hello#World"
console.log(decode("11#Hello#World")); // ["Hello#World"]

// Best Practices : Length delimiter 
// Complexity Analysis : Time Complexity: O(N) , Space Complexity: O(N)
