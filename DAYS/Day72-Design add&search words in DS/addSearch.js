// Binary Tree :Design an Add and Search data structure(LeetCode 211) 
// Given a data structure that supports adding new words and searching for words with '.' as a wildcard character.
// Example 1: Input ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
// Output: [null,null,null,true,false,true,true,false,false]

// Different Approach: 
// 1. Using Trie Data Structure - Time O(m) , Space O(m) 
// Leetcode Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
// Solution:
function TrieNode() {
    this.children = {};
    this.isEndOfWord = false;
}
function WordDictionary() {
    this.root = new TrieNode();
}
WordDictionary.prototype.addWord = function(word) {
    let  node = this.root;
    for (let char of word){
        if(!node.children[char]){
            node.children[char]=new TrieNode();
        }
        node=node.children[char];
    }
    node.isEndOfWord = true;
}
WordDictionary.prototype.search = function(word) {
    dfs = (index, node) => {
        if(index === word.length){
            return node.isEndOfWord;
        }
        let char = word[index];
        if(char === '.'){
            for(let child in node.children){
                if(dfs(index+1, node.children[child])){
                    return true;
                }
            }
            return false;
        } else if(char in node.children){
            return dfs(index+1, node.children[char]);
        }
        return false;

    };
    return dfs(0, this.root);
};
// Test Cases
let wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
console.log(wordDictionary.search("pad"));  // Output: False
console.log(wordDictionary.search("bad"));  // Output: True
console.log(wordDictionary.search(".ad"));  // Output: True
console.log(wordDictionary.search("gap"));  // Output: False
console.log(wordDictionary.search("bad"));  // Output: True
console.log(wordDictionary.search("b.."));  // Output: True
// Example 1: Input ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]

// Complexity Analysis: Time complexity: addWord - O(m), search - O(26^n) , Space complexity: O(m)