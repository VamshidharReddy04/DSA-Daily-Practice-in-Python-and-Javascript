# Graphs - Course Schedule
# Given the total number of courses and a list of prerequisite pairs, 
# determine if it is possible to finish all courses.
# Example 1: Input: numCourses = 2, prerequisites = [[1,0]] Output: true
# Example 2: Input: numCourses = 2, prerequisites = [[1,0],[0,1]] Output: false
# Different approach:  
# 1. DFS (Cycle Detection in Directed Graph) - Time O(V+E), Space O(V+E) -V is vertices and E is edges
# 2. BFS with In-Degree(Kahn's Algorithm) - Time O(V+E), Space O(V+E) - V is vertices and E is edges

# Solution 2: BFS with In-Degree(Kahn's Algorithm)
# Leetcode Link: https://leetcode.com/problems/course-schedule/
from collections import deque  # importing defaultdict and deque from collections module
class Solution:
    def courseSchedule(self,numCourses,prerequisites):
        indegree =[0]*numCourses # creating an array of size numCourses and initializing it with 0
        graph={i:[] for i in range(numCourses)} # creating a graph using dictionary comprehension
        for course,pre in prerequisites: 
            graph[pre].append(course) #adding the course to the graph
            indegree[course] += 1 # updating the indegree of the course
        
        queue=deque([i for i in range(numCourses) if indegree[i]==0 ]) # creating a queue and adding all the courses with indegree 0
        count = 0 
        while queue:
            curr=queue.popleft() # popping the first element from the queue
            count += 1 # incrementing the count
            for nei in graph[curr]: # iterating through the neighbors of the current course
                indegree[nei] -=1 # decrementing the indegree of the neighbor
                if indegree[nei]== 0 : # if the indegree of the neighbor is 0
                    queue.append(nei) # adding the neighbor to the queue
        return count == numCourses # if the count is equal to numCourses, return True else return False
# Test Cases
print(Solution().courseSchedule(2, [[1,0]])) # True
print(Solution().courseSchedule(2, [[1,0],[0,1]])) # False
print(Solution().courseSchedule(4, [[1,0],[2,1],[3,2]])) # True

# Best Approach: BFS with In-Degree(Kahn's Algorithm)
# Complexity Analysis: Time Complexity: O(V + E) where V is the number of vertices (courses) and E is the number of edges (prerequisites).
# Space Complexity: O(V + E) for storing the graph and the indegree array.
