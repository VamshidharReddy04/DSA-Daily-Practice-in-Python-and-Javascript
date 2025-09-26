//  Linked List - Merge k Sorted Lists (Leetcode Problem #23)
// Given an array of k linked-lists lists, each linked-list is sorted in ascending order.
// Merge all the linked-lists into one sorted linked-list and return it.
// Example 1: Input: lists = [[1,4,5],[1,3,4],[2,6]] Output: [1,1,2,3,4,4,5,6]
// Example 2: Input: lists = [] Output: []
// Example 3: Input: lists = [[]] Output: []
// Diiferent Approaches:
// 1.Brute Force: Time O(k*n) Space O(1)
// 2.Sequential Merge: Time O(k^2*n) Space O(1)
// 3.Min-Heap/Priority Queue:Time O(nlog(k)) Space O(k)
// 4.Divide and Conquer: Time O(n*k*log(k)) Space O(1)
// Solution 3: Min-Heap/Priority Queue
// Leetcode Link: https://leetcode.com/problems/merge-k-sorted-lists/

// Definition for singly-linked list
function ListNode(val, next = null) {
    this.val = val;
    this.next = next;
}
function mergeKSorted(lists) {
    let minHeap = [];
    let dummy = new ListNode(-1);
    let tail = dummy;
    // Initialize heap with first node of each list
    lists.forEach((node, idx) => {
        if (node)minHeap.push([node.val, idx, node]);
    });
    while (minHeap.length > 0) {
        let [val, idx, node] = minHeap.pop(); // pop smallest element
        tail.next = node;
        tail = tail.next;
        if (node.next) {
            minHeap.push([node.next.val, idx, node.next]);
        }
    }
    return dummy.next;
}
// Helper function to print linked list
function printListNode(head) {
    let val = [];
    while (head) {
        val.push(head.val);
        head = head.next;
    }
    console.log(val);
}

// Test Cases
let list1 = new ListNode(1, new ListNode(4, new ListNode(5)));
let list2 = new ListNode(1, new ListNode(3, new ListNode(4)));
let list3 = new ListNode(2, new ListNode(6));
let lists = [list1, list2, list3];
printListNode(mergeKSorted(lists)); // [1,1,2,3,4,4,5,6]

lists = [];
printListNode(mergeKSorted(lists)); // []

lists = [null];
printListNode(mergeKSorted(lists)); // []

// Best Approach: Min-Heap/Priority Queue
// Complexity Analysis: Time Complexity: O(N log k) , Space Complexity: O(k)
