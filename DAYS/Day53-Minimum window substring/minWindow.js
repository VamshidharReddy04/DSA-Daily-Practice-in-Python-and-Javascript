// Strings : Minimum Window Substring leetcode 76
// Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
// The testcases will be generated such that the answer is unique.
// Example 1: Input: s = "ADOBECODEBANC", t = "ABC" Output: "BANC"
// Example 2: Input: s = "a", t = "a" Output: "a"
// Example 3: Input: s = "a", t = "aa" Output: "" Explanation: Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.

// Different Approaches
// 1. Brute Force - Time O(n^3) Space O(1)
// 2. Sliding Window - Time O(n) Space O(1)
// 3. Optimized Sliding Window - Time O(n) Space O(1)

// Solution - Sliding Window
function minWindow(s, t) {
    if(s.length<t.length) return "";
    const count=new Map() , window=new Map();
    for (let char of t){
        count.set(char,(count.get(char) || 0)+1);
    }
    let have=0,need=count.size;
    let left=0,right=0;
    let res=[-1,-1];
    let resLen=Infinity;
    for(let right=0;right<s.length;right++){
        const char=s[right];
            window.set(char,(window.get(char)||0)+1);
            if(count.has(char) && window.get(char)===count.get(char)){
                have++;
            }
            while(have===need){
                if((right-left+1)<resLen){
                    res=[left,right];
                    resLen=right-left+1;
                }
            const leftChar=s[left];
            window.set(leftChar,window.get(leftChar)-1);
            if(count.has(leftChar) && window.get(leftChar)<count.get(leftChar)){
                have--;
            }
            left++;
        }
    }
    const [l,r]=res;
    return l===-1 ? "" : s.substring(l,r+1);
}
// Test Cases
console.log(minWindow("ADOBECODEBANC", "ABC")); // Output: "BANC"
console.log(minWindow("a", "a")); // Output: "a"
console.log(minWindow("a", "aa")); // Output: ""

// Best Approach : Sliding Window
// Complexity Analysis: Time Complexity: O(n) , Space Complexity: O(1)