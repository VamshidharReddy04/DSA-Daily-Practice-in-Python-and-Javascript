// Heap : Median of a Data Stream (LeetCode 295)
// Given two heaps, a max-heap to store the lower half of the numbers
// Example 1: Input: ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"] [[],[1],[2],[],[3],[]] Output: [null,null,null,1.5,null,2.0]
// Different Approaches:
// 1. Using two heaps (max-heap for lower half, min-heap for upper half)
// 2. Using a sorted list (less efficient for large data streams)
// LeetCode Link: https://leetcode.com/problems/median-of-a-data-stream/
// Solution:
function MaxHeap() {
    this.heap = [];
}
MaxHeap.prototype = {
    addNum: function(num) {
        if (this.heap.length === 0 || num <= this.getMax()) {
            this.heap.push(num);
            this.heap.sort((a, b) => b - a);
        } else {
            this.heap.push(num);
            this.heap.sort((a, b) => b - a);
        }
    },
    findMedian: function() {
        if (this.heap.length % 2 === 1) {
            return this.heap[Math.floor(this.heap.length / 2)];
        } else {
            return (this.heap[this.heap.length / 2 - 1] + this.heap[this.heap.length / 2]) / 2;
        }
    }
};
MaxHeap.prototype.getMax = function() {
    return this.heap[0];
};
// Test Cases
const medianFinder = new MaxHeap();
medianFinder.addNum(1);
medianFinder.addNum(2);
console.log(medianFinder.findMedian()); // Output: 1.5
medianFinder.addNum(3);
console.log(medianFinder.findMedian()); // Output: 2.0

// Complexity Analysis: Time Complexity: O(log n) for addNum, O(1) for findMedian
// Space Complexity: O(n) for storing the numbers in the heaps