# String encoding and decoding leetcode(271)
# Given a string, design an algorithm to encode it and decode it.The encoded string is given as input to the decode function.
# Example 1: Input: "Hello" Output: "5#Hello" 
# Example 2: Input: "Hello World" Output: "5#Hello 5#World"
# Different Approach:
# 1. Join using Delimiter - Time O(N) Space O(N)
# 2. Length delimiter - Time O(N) Space O(N)
# Leetcode Link: https://leetcode.com/problems/encode-and-decode-strings/
# Solution :

def encode(strs):
    return ''.join(f'{len(s)}#{s}' for s in strs)  # '#'is add as a delimiter
def decode(s):
    res,i=[],0  # res to store result and i as index
    while i<len(s):
        j=i # j to find the delimiter '#'
        while s[j]!="#":
            j+=1 
        length=int(s[i:j]) # length of the string
        res.append(s[j+1:j+1+length]) # extract the string using length
        i=j+1+length # move i to the next string start
    return res
# Test cases
encoded_str = encode(["Hello","World", "I ","am"])
decoded_str = decode(encoded_str)
print(encoded_str) # "5#Hello5#World1#I2#am"
print(decoded_str) # ["Hello","World", "I ","am"]

# Best Approach: Length Delimiter
# Complexity Analysis: Time Complexity: O(N) , Space Complexity: O(N)
