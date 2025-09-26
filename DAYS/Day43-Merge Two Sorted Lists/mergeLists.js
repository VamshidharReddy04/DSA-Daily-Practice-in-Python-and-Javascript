// Linked List- Merge Two Sorted Lists (LeetCode Problem 21)
// You are given the heads of two sorted linked lists list1 and list2.
// Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
// Return the head of the merged linked list.
// Example 1:Input: list1 = [1,2,4], list2 = [1,3,4] Output: [1,1,2,3,4,4]
// Example 2:Input: list1 = [], list2 = [] Output: []
// Example 3:Input: list1 = [], list2 = [0] Output: [0]

// Different Approaches:
// 1. Iterative Approach ( Two Pointers)-> Time Complexity: O(n), Space Complexity: O(1)
// 2. Recursive Approach (merge )-> Time Complexity: O(n), Space Complexity: O(n)
// Solution 1: Iterative Approach
// LeetCode Link: https://leetcode.com/problems/merge-two-sorted-lists/solutions/2295015/javascript-iterative-and-recursive-solution-with-explanation/?orderBy=most_relevant

class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}
function mergeTwoLists(list1, list2) {
    let dummy = new ListNode(0); // Dummy node to simplify merging
    let tail = dummy;           // Tail pointer for the merged list
    while (list1 && list2) {      
        if (list1.val < list2.val) {  // Compare values to decide which node to add
            tail.next = list1;        // Append the smaller node to the merged list
            list1 = list1.next;     // Move the pointer in list1 forward
        } else {
            tail.next = list2;      // Append the smaller node to the merged list
            list2 = list2.next;     // Move the pointer in list2 forward
        }
        tail = tail.next;           // Move the tail pointer forward
    }
    tail.next = list1 ? list1 : list2; // Append any remaining nodes
    return dummy.next;                  // Return the head of the merged list
}
// Helper function to print linked list
function printList(head) {   // Converts linked list to array for easy visualization
    let current = head;      // Pointer to traverse the list
    let result = [];    // Array to store the values
    while (current) {
        result.push(current.val);   // Add current node's value to the array
        current = current.next; // Move to the next node
    }
    return result;
}
// Test Cases
let list1 = new ListNode(1, new ListNode(2, new ListNode(4)));
let list2 = new ListNode(1, new ListNode(3, new ListNode(4)));
let mergedList = mergeTwoLists(list1, list2);
console.log(printList(mergedList)); // Output: [1, 1, 2, 3, 4, 4]
// Example 2
list1 = null;
list2 = null;
mergedList = mergeTwoLists(list1, list2);
console.log(printList(mergedList)); // Output: []
// Example 3
list1 = null;
list2 = new ListNode(0);
mergedList = mergeTwoLists(list1, list2);
console.log(printList(mergedList)); // Output: [0]

// Best Approach : Iterative Approach (Two Pointers)
// Complexity Analysis: Time Complexity: O(n) | Space Complexity: O(1)