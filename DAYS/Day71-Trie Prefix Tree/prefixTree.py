# Binary Tree : Implementation of a Prefix Tree (Leetcode 208)
# Given a set of strings, implement a prefix tree with insert, search, and startsWith methods.
# Example 1: Input: ["PrefixTree","insert","search","search","startsWith","insert","search"]
#          [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
# Output: [null,null,true,false,true,null,true]
# Different Approaches: 
# 1. Trie (Prefix Tree)- Time O(m), Space O(m) 
# Leetcode Link: https://leetcode.com/problems/implement-trie-prefix-tree/
# Solution:

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.isEnd = True
    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children: return False
            node=node.children[char]
        return node.isEnd
    def startsWith(self,prefix):
        node=self.root
        for char in prefix:
            if char not in node.children: return False
            node=node.children[char]
        return True
# Test Cases
trie=Trie()
trie.insert("apple")
print(trie.search("apple"))   # True
print(trie.search("app"))     # False
print(trie.startsWith("app")) # True
trie.insert("app")
print(trie.search("app"))     # True

# Complexity Analysis: Time Complexity: O(m) , Space Complexity: O(m) 