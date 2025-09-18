# BackTracking : Combination Sum
# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# Example 1: Input: candidates = [2,3,6,7], target = 7 Output: [[2,2,3],[7]] 
# Example 2: Input: candidates = [2,3,5], target = 8 Output: [[2,2,2,2],[2,3,3],[3,5]] 
# Example 3: Input: candidates = [2], target = 1 Output: []

# Different Approaches:
#  1. Recursion (Brute Force)
#  2. Backtracking (Optimized)
# Leetcode Link : https://leetcode.com/problems/combination-sum/
class Solution:
    @staticmethod
    def combinationSum(candidates, target):
        result = []  # To store the final result
        candidates.sort()  # Sort the candidates
        def backtrack(start, path, target):
            if target == 0:  # If we found a combination
                result.append(path[:])  # Append a copy of the current path to result
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target: # If the current candidate is greater than the remaining target
                    break
                backtrack(i, path + [candidates[i]], target - candidates[i])
        backtrack(0, [], target)
        return result
# Test Cases
print(Solution.combinationSum([2,3,6,7],7)) # [[2,2,3],[7]]
print(Solution.combinationSum([2,3,5],8)) # [[2,2,2,2],[2,3,3],[3,5]]
print(Solution.combinationSum([2],1)) # []

# Best Approach : Backtracking
# Complexity Analysis : Time - O(n^target), Space - O(target)
