//Intervals- Insert interval
// Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
// Example 1: Intervals: [[1,3],[6,9]], New Interval: [2,5] -Output: [[1,5],[6,9]] 
// Example 2: Intervals: [[1,2],[3,5],[6,7],[8,10],[12,16]], New Interval: [4,8] - Output: [[1,2],[3,10],[12,16]]

// Different Approaches:
// 1. Brute Force Approach -Time Complexity: O(nlogn) - Space Complexity: O(n)
// 2. Optimal Approach - Time Complexity: O(n) - Space Complexity: O(n)

// Solution 2: Optimal Approach
function insertInterval(intervals,newInterval){
    let result = [];
    for (let i=0;i<intervals.length;i++){
        if (intervals[i][1]<newInterval[0]){
            result.push(intervals[i])
        }
        else if(intervals[i][0]>newInterval[1]){
            result.push(newInterval);
            newInterval = intervals[i];
        }
        else{
            newInterval[0]=Math.min(intervals[i][0],newInterval[0]);
            newInterval[1]=Math.max(intervals[i][1],newInterval[1]);
        }
    }
    result.push(newInterval);
    return result;
}
// Test Cases:
console.log(insertInterval([[1,3],[6,9]],[2,5])); // [[1,5],[6,9]]
console.log(insertInterval([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])); // [[1,2],[3,10],[12,16]]

// Best Solution: Optimal Approach
// Complexity Analysis: Time Complexity: O(n) - Space Complexity: O(n)