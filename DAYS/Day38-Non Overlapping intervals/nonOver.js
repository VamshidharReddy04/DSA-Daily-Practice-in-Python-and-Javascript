// Intervals - Non-overlapping Intervals
// Type of Problem: Greedy + Interval Scheduling
// Given an array of intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
// Example 1: Input: intervals = [[1,2],[2,3],[3,4],[1,3]] Output: 1 Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
// Example 2: Input: intervals = [[1,2],[1,2],[1,2]] Output: 2 
// Example 3: Input: intervals = [[1,2],[2,3]] Output: 0
// Different Approaches: 
// 1.Brute Force - Time Complexity: O(n^2) Space Complexity: O(1)
// 2.Greedy - Time Complexity: O(n log n) Space Complexity: O(1)

// Solution 2: Greedy
function nonOver(intervals){
    if (!intervals || intervals.length === 0) return 0;
    intervals.sort((a, b) => a[1] - b[1]);
    let count = 0;
    let end = intervals[0][1];
    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i][0] < end) {
            count++;
        } else {
            end = intervals[i][1];
        }
    }
    return count;
}
// Test Cases
console.log(nonOver([[1,2],[2,3],[3,4],[1,3]])); // Output: 1
console.log(nonOver([[1,2],[1,2],[1,2]])); // Output: 2
console.log(nonOver([[1,2],[2,3]])); // Output: 0

// Best Approach: Greedy
// Complexity Analysis : Time Complexity: O(n log n) Space Complexity: O(1)