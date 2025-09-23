# Graphs - Alien Dictionary
# Given a list of words from the alien language's dictionary, where the words are sorted lexicographically 
# by the rules of this new language, derive the order of letters in this language.
# Example 1: Input: ["wrt","wrf","er","ett","rftt"] Output: "wertf"
# Example 2: Input: ["z","x"] Output: "zx"
# Example 3: Input: ["z","x","z"] Output: "" (invalid order)
# Different Aproaches:
# 1. Topological Sort using Kahn's Algorithm (BFS)
# 2. Topological Sort using DFS

# Topological Sort solution using Kahn's Algorithm (BFS)
# Leetcode: https://leetcode.com/problems/alien-dictionary/

from collections import deque
class Solution:
    def alienOrder(words):
        if not words:
            return ""
        graph={c :set() for word in words for c in word} # adjacency list
        indegree={c:0 for c in graph} # indegree count

        for i in range(len(words)-1): 
            w1,w2=words[i],words[i+1]  #w1 is before w2
            if len(w1)>len(w2) and w1.startswith(w2): 
                return "" # invalid case
            for j in range(min(len(w1),len(w2))):
                if w1[j]!=w2[j]: # first different char
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j]) # add edge
                        indegree[w2[j]]+=1 # increase indegree
                    break
        queue=deque([c for c in indegree if indegree[c]==0]) # all chars with 0 indegree
        order=[]
        while queue: 
            c=queue.popleft() # char with 0 indegree
            order.append(c) # add to order
            for nei in graph[c]: # reduce indegree of neighbors
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei) # add to queue if indegree is 0
        if len(order)==len(indegree): # cycle detected
            return "".join(order) # valid order
        else:
            return "" # invalid order due to cycle

# Test Cases
print(Solution.alienOrder(["wrt","wrf","er","ett","rftt"])) # Output: "wertf"
print(Solution.alienOrder(["z","x"])) # Output: "zx"
    
# Best Approach: Topological Sort using Kahn's Algorithm (BFS)
# Complexity Analysis: Time: O(V + E), Space: O(V + E)  
# where V is the number of unique characters and E is the number of edges in the graph.