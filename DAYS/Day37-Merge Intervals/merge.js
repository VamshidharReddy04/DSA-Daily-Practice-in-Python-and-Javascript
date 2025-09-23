// Intervals - Merge Overlapping Intervals
// Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
// Example 1: Input: intervals = [[1,3],[2,6],[8,10],[15,18]] Output: [[1,6],[8,10],[15,18]]
// Example 2: Input: intervals = [[1,4],[4,5]] Output: [[1,5]] 

// Different Approaches:
// 1. Sorting and Merging - Time Complexity: O(n log n) , Space Complexity: O(n)
// 2. Using a Stack - Time Complexity: O(n log n) , Space Complexity: O(n)
// 3. Sweep Line Algorithm - Time Complexity: O(n log n) , Space Complexity: O(n)

// Solution 1: Sorting and Merging
function mergeIntervals(intervals) {
    if(intervals.length ===0) return [];
    intervals.sort((a,b)=>a[0]-b[0]);
    const merged=[];
    for(const interval of intervals){
        if (!merged.length || merged[merged.length-1][1]<interval[0]){
            merged.push(interval);
        }
        else{
            merged[merged.length-1][1]=Math.max(merged[merged.length-1][1],interval[1]);
        }
    }
    return merged;
}
// Test Case:
console.log(mergeIntervals([[1,3],[2,6],[8,10],[15,18]])); // Output: [[1,6],[8,10],[15,18]]
console.log(mergeIntervals([[1,4],[4,5]])); // Output: [[1,5]]
// Best Approach: Sorting and Merging
// Complexity Analysis: Time Complexity: O(n log n) , Space Complexity: O(n)
