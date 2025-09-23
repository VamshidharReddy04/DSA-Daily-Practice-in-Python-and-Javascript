# Graphs - Number of Connected Components in an Undirected Graph
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to find the number of connected components in an undirected graph.
# Example 1: Input: n = 5 edges = [[0, 1], [1, 2], [3, 4]] Output: 2
# Example 2: Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [3, 4]] Output: 1
# Different Approaches: 
# 1. Depth-First Search (DFS) / Breadth-First Search (BFS)
# 2. Union-Find (Disjoint Set Union - DSU)

# Solution using Depth-First Search (DFS)
# Leetcode: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
class Solution:
    def countCompoents(n,edges):
        adj={i:[] for i in range(n)} # Adjacency list representation of the graph
        for u,v in edges: # Building the adjacency list
            adj[u].append(v)
            adj[v].append(u)
        visit=set() # Set to keep track of visited nodes
        def dfs(node):
            for nei in adj[node]: # Explore all neighbors
                if nei not in visit:
                    visit.add(nei)  # Mark the neighbor as visited
                    dfs(nei)    # Recursively visit the neighbor
        count=0
        for i in range(n):
            if i not in visit:
                count+=1    # Found a new connected component
                visit.add(i) # Mark the node as visited
                dfs(i) # Perform DFS to visit all nodes in this component
        return count
# Test Case
print(Solution.countCompoents(5, [[0, 1], [1, 2], [3, 4]]))  # Output: 2
print(Solution.countCompoents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))  # Output: 1

#Complexity Analysis : Time Complexity: O(N + E) , Space Complexity: O(N + E)
# N is the number of nodes and E is the number of edges in the graph.