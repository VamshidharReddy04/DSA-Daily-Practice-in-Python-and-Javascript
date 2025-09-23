# Graphs- Graph Valid Tree
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
# Example 1: Input: n = 5, edges = [[0,1], [0,2], [0,3], [1,4]] Output: true
# Example 2: Input: n = 5, edges = [[0,1], [1,2], [2,3], [1,3], [1,4]] Output: false
# Different Approaches:
# 1. Depth-First Search (DFS)
# 2. Breadth-First Search (BFS)
# 3. Union-Find

# Solution 1: Depth-First Search (DFS)
# Leetcode: https://leetcode.com/problems/graph-valid-tree/solutions/1673731/python-dfs-bfs-union-find-with-explanation/
class Solution:
    def vaildTree(n,edges):
        if not n :return False
        adj={i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2) # undirected graph
            adj[n2].append(n1)
        visit=set()
        def dfs(i,prev):
            if i in visit:  # cycle
                return False
            visit.add(i)    # mark as visited
            for nei in adj[i]:
                if nei==prev: # skip the parent node
                    continue
                if not dfs(nei,i): # if cycle detected in the subtree
                    return False
            return True
        return dfs(0,-1) and len(visit)==n # check if all nodes are visited
# Test Cases
print(Solution.vaildTree(5, [[0,1], [0,2], [0,3], [1,4]])) # True
print(Solution.vaildTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]])) # False
print(Solution.vaildTree(1, [])) # True

# Best Solution - DFS/ BFS
# Complexity Analysis: Time O(n) | Space O(n)
