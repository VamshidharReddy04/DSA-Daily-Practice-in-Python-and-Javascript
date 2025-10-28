// Binary Tree : Implementation of a Prefix Tree (Leetcode 208)
// Given a set of strings, implement a prefix tree with insert, search, and startsWith methods.
// Example 1: Input: ["PrefixTree","insert","search","search","startsWith","insert","search"]
// Output: [null,null,true,false,true,null,true]
// Different Approaches:
// 1. Trie (Prefix Tree) Implementation-Time O(m), Space O(m)
// 2. HashMap Implementation-Time O(m), Space O(m)
// Leetcode Link: https://leetcode.com/problems/implement-trie-prefix-tree/
// Solution:

function TrieNode() {
    this.children = {};
    this.isEndOfWord = false;
}

function Trie() {
    this.root = new TrieNode();
}
Trie.prototype.insert = function(word) {
    let node = this.root;
    for (const char of word) {
        if (!node.children[char]) {
            node.children[char] = new TrieNode();
        }
        node = node.children[char];
    }
    node.isEndOfWord = true;
};

Trie.prototype.search = function(word) {
    let node = this.root;
    for (const char of word) {
        if (!node.children[char]) return false;
        node = node.children[char];
    }
    return !!node.isEndOfWord;
};

Trie.prototype.startsWith = function(prefix) {
    let node = this.root;
    for (const char of prefix) {
        if (!node.children[char]) return false;
        node = node.children[char];
    }
    return true;
};
// Test Cases
let trie = new Trie();
trie.insert("apple");
console.log(trie.search("apple")); // returns true
console.log(trie.search("app"));   // returns false
console.log(trie.startsWith("app")); // returns true
trie.insert("app");
console.log(trie.search("app"));   // returns true  

// Complexity Analysis : Time Complexity: O(m) , Space Complexity: O(m) 