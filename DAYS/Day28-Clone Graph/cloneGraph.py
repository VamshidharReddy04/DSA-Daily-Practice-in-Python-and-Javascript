# Graphs : Clone Graph
# Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# Example 1: input: adjList = [[2,4],[1,3],[2,4],[1,3]] Output: [[2,4],[1,3],[2,4],[1,3]]
# Example 2: input: adjList = [[]] Output: [[]]

# Different Approaches:
# 1. DFS using Recursion - Time: O(N) Space: O(N)
# 2. DFS using Stack - Time: O(N) Space: O(N)
# 3. BFS using Queue - Time: O(N) Space: O(N)

# Solution 1: DFS using Recursion
# Leetcode: https://leetcode.com/problems/clone-graph/description/

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node: return None  # if node is None return None
        old_to_new = {}  # old node to new node mapping
        def clone(n):
            if n in old_to_new:
                return old_to_new[n] # if node is already cloned return the cloned node
            copy = Node(n.val) # create a new node with the value of the old node
            old_to_new[n] = copy # map the old node to the new node

            for nei in n.neighbors: # iterate through the neighbors of the old node
                copy.neighbors.append(clone(nei)) # append the cloned neighbor to the new node's neighbors list
            return copy
        return clone(node)
# Test Cases:
print(Solution().cloneGraph(Node(1, [Node(2), Node(4)])))
print(Solution().cloneGraph([[2,4],[1,3],[2,4],[1,3]])) 
print(Solution().cloneGraph(Node(1, [])))  
# Best Approach: DFS using Recursion
# Complexity Analysis: Time Complexity: O(N) Space Complexity: O(N)