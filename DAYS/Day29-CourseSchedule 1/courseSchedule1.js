// Graphs - Course Schedule I
// Given the total number of courses and a list of prerequisite pairs, determine if it is possible to finish all courses.

// Example 1: Input: numCourses = 2, prerequisites = [[1,0]] Output: true
// Example 2: Input: numCourses = 2, prerequisites = [[1,0],[0,1]] Output: false
// Different Approaches:
// 1 . DFS (Cycle Detection in Directed Graph) - Time O(v+n) Space O(v+n)
// 2 . BFS (Kahn's Algorithm) - Time O(v+n) Space O(v+n)

// Solution 2: BFS (Kahn's Algorithm)
function courseSchedule(numCourses, prerequisites) {
  let graph = new Map(); // adjacency list representation of the graph
  let indegree = new Array(numCourses).fill(0); // array to keep track of in-degrees of each vertex
  for (let [course, pre] of prerequisites) {
    if (!graph.has(pre))
      // if the prerequisite course is not in the graph, add it with an empty array
      graph.set(pre, []);
    graph.get(pre).push(course); // add the course to the prerequisite course's array
    indegree[course]++; // increment the in-degree of the course
  }
  let queue = []; // queue to keep track of courses with in-degree 0
  for (let i = 0; i < numCourses; i++) {
    if (indegree[i] === 0)
      // if the in-degree of the course is 0, add it to the queue
      queue.push(i);
  }
  let count = 0; // counter to keep track of the number of courses that can be completed
  while (queue.length) {
    let course = queue.shift(); // remove the first course from the queue
    count++; // increment the counter
    if ((graph.has(course))) {
      // if the course has any dependent courses
      for (let nextCourse of graph.get(course)) {
        indegree[nextCourse]--; // decrement the in-degree of the dependent course
        if (indegree[nextCourse] === 0) {
          queue.push(nextCourse); // if the in-degree of the dependent course is 0, add it to the queue
        }
      }
    }
  }
  return count === numCourses; // return true if the number of courses that can be completed is equal to the total number of courses
}
// Test Cases
console.log(courseSchedule(2, [[1, 0]])); // True
console.log(courseSchedule(2, [[1, 0],[0, 1]])); // False
console.log(courseSchedule(4, [[1, 0],[2, 1],[3, 2],])); // True
// Best Approach: BFS with In-Degree(Kahn's Algorithm)
// Complexity Analysis: Time Complexity: O(V + E) where V is the number of vertices (courses) and E is the number of edges (prerequisites).
// Space Complexity: O(V + E) for storing the graph and the indegree array.
