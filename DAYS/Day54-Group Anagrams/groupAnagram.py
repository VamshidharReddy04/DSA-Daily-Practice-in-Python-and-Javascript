# String - Group Anagrams leetcode 49
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1: Input: strs = ["eat","tea","tan","ate","nat","bat"] Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2: Input: strs = [""] Output: [[""]]
# String - Group Anagrams leetcode 49
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1: Input: strs = ["eat","tea","tan","ate","nat","bat"] Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2: Input: strs = [""] Output: [[""]]

# Different approaches:
# 1. Sorting Approach: Time O(NKlogK) Space O(NK)
# 2. Counting Approach: Time O(NK) Space O(NK)

# Solution 2: Counting Approach
# Leetcode https://leetcode.com/problems/group-anagrams/solutions/1678829/python-counting-approach-with-explanation/?orderBy=most_relevant
from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    for word in strs:
        count = [0] * 26  # There are 26 letters in the English alphabet
        for char in word:
            count[ord(char) - ord('a')] += 1  # Increment count alphabet index
        key = tuple(count)
        anagram_map[key].append(word)  # Add word to group
    return list(anagram_map.values())

# Test Cases
if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Output groups
    print(groupAnagrams([""]))  # Output [[""]]

# Best Approach: Counting Approach
# Complexity Analysis: Time complexity: O(NK) , Space complexity: O(NK)