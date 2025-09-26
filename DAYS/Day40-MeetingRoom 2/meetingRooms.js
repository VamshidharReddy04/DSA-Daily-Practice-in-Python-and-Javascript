// Intervals : Meeting Rooms II
// Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
// find the minimum number of conference rooms required.

// Example 1: Input: [[0, 30],[5, 10],[15, 20]] Output: 2
// Example 2: Input: [[7,10],[2,4]] Output: 1
// Different Approaches:
// 1. Using Min-Heap (Priority Queue) - Time Complexity: O(N log N) Space Complexity: O(N)
// 2. Two Pointers Approach- Time Complexity: O(N log N) Space Complexity: O(N)

// Solution 1: Using Min-Heap (Priority Queue)
// Leetcode Link: https://leetcode.com/problems/meeting-rooms-ii/

function meetingRooms(intervals){
    if (!intervals ||intervals === 0) return 0;
    // Sort the intervals by start time
    intervals.sort((a,b)=>a[0]-b[0]);
    const heap=[];
    // Add the end time of the first meeting
    const pushHeap=(val)=>{ // Min-Heap Push
        heap.push(val); 
        heap.sort((a,b)=>a-b); // Keep the heap sorted
    }
    const popHeap=()=>{ // Min-Heap Pop
        return heap.shift();
    }
    for (const interval of intervals){
        if (heap.length && interval[0]>=heap[0]){ // If the room is free, reuse it
            popHeap(); // Remove the earliest ending meeting
        }
        pushHeap(interval[1]); // Allocate a new room
    }
    return heap.length; // The size of the heap is the number of rooms needed
}
// Test Cases
console.log(meetingRooms([[0, 30],[5, 10],[15, 20]])); // Output: 2
console.log(meetingRooms([[7,10],[2,4]])); // Output: 1

// Best Approach: Min-Heap (Priority Queue) 
// Complexity Analysis: Time Complexity: O(N log N) Space Complexity: O(N)