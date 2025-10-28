# Binary Tree : Design add and search words data structure (LeetCode 211)
# Given a data structure that supports the following two operations: void addWord(word) and bool search(word)
# Example 1: Input ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
# Output [null,null,null,true,false,true,true,false,false]

# Different Approaches:
# 1. Trie (Prefix Tree) Implementation
# 2. HashSet with Wildcard Matching
# LeetCode Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Solution:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.is_end_of_word=True
    def search(self,word):
        def dfs(index,node):
            if index==len(word): return node.is_end_of_word
            char=word[index]
            if char=='.':
                for child in node.children.values():
                    if dfs(index+1,child): return True
                return False
            else:
                if char not in node.children: return False
                return dfs(index+1,node.children[char])
        return dfs(0,self.root)
# Test Cases
wordDictionary=Solution()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
print(wordDictionary.search("pad"))  # Output: False
print(wordDictionary.search("bad"))  # Output: True
print(wordDictionary.search(".ad"))  # Output: True
print(wordDictionary.search("gap"))  # Output: False
print(wordDictionary.search("bad"))  # Output: True
print(wordDictionary.search("b.."))  # Output: True
# Example 1: Input ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]

# Complexity Analysis: Time complexity: addWord - O(m), search - O(26^n) , Space complexity: O(m)
