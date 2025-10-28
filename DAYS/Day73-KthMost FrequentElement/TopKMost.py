# Heap- Kth Most Frequent Elements (LeetCode 347)
# Given a non-empty array of integers, return the k most frequent elements.
# Example 1: Input: nums = [1,1,1,2,2,3], k = 2 Output: [1,2]
# Example 2: Input: nums = [1], k = 1 Output: [1]

# Different Approaches:
# 1. Using HashMap and Min-Heap- O(N log K) time and O(N) space
# 2. Using HashMap and Bucket Sort- O(N) time and O(N)
# Leetcode Link: https://leetcode.com/problems/top-k-frequent-elements/
# Solution:
from collections import Counter
class Solution:
    def topKFrequent(nums,k):
        freq=Counter(nums) # HashMap to store frequency of each element
        bucket=[[] for _ in range(len(nums)+1)] # Bucket to store elements based on frequency
        for num, count in freq.items():
            bucket[count].append(num) # Append elements to their respective frequency bucket
        result=[]               # To store the result
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:      
                result.append(num) # Append elements with current frequency
                if len(result)==k: # If we have k elements, return the result
                    return result

# Test Cases
print(Solution.topKFrequent([1,1,1,2,2,3],3)) # [1,2,3]
print(Solution.topKFrequent([1],1)) # [1]

# Complexity Analysis: Time Complexity: O(N) Space Complexity: O(N)