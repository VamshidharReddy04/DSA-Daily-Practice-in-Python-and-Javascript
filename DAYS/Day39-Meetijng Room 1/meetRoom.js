// Internvals - Meeting Room 1
// Type of problem:Interval Scheduling , Overlap Intervals
// Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
// determine if a person could attend all meetings.
// Example 1: Input: [[0,30],[5,10],[15,20]] Output: Flase
// Example 2: Input: [[7,10],[2,4]] Output: True

// Different Approaches:
// 1. Sort the intervals by start time and end time (Greedy Approach)-Time: O(NlogN) Space: O(1)
// 2. Use a min-heap to keep track of end times of meetings (Sweep Line Algorithm)-Time: O(NlogN) Space: O(N)
// Solution 1 : Sorting

function attendMeetings(intervals){
    intervals.sort((a,b)=>a[0]-b[0]); // Sort by start time
    for( i=1;i<intervals.length;i++){
        if(intervals[i][0]<intervals[i-1][1]) // Overlapping intervals
        return false;
    }
    return true;   
}
// Test Cases
console.log(attendMeetings([[0,30],[5,10],[15,20]])); // False
console.log(attendMeetings([[7,10],[2,4]])); // True

// Best Approach: Sorting 
// complexity Analysis: Time: O(NlogN) Space: O(1)
