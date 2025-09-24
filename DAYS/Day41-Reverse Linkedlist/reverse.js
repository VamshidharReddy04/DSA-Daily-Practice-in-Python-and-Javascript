// Linked List - Reverse a Linked List
// Type of problem: Linked List manipulation, pointer Reversal
// Given the head of a singly linked list, reverse the list, and return the reversed list.
// Example 1: Input: head = [1,2,3,4,5] Output: [5,4,3,2,1]
// Example 2: Input: head = [1,2] Output: [2,1]
// Example 3: Input: head = [] Output: []

// Different Approaches:
// 1. Iterative Approach - Time Complexity: O(n), Space Complexity: O(1)
// 2. Recursive Approach - Time Complexity: O(n), Space Complexity: O(n)    

// Solution 1: Iterative Approach
// Leecode: https://leetcode.com/problems/reverse-linked-list/
function ListNode(val, next = null) {
    this.val = val;
    this.next = next;
}
function reverse(head) {
    let prev =null;
    let curr =head;
    while(curr){ // Traverse the list
        let next=curr.next; // Store next node
        curr.next=prev; // Reverse current node's pointer
        prev=curr;     // Move pointers one position ahead
        curr=next;  // Move to next node
    }
    return prev;
}
// Helper function to print linked list values
function printList(head) {
    let values = [];
    let curr = head;
    while (curr) {
        values.push(curr.val);
        curr = curr.next;
    }
    console.log(values);
}
// Test Cases - Create linked lists manually
// Test 1: [1,2,3,4,5]
let node5 = new ListNode(5);
let node4 = new ListNode(4, node5);
let node3 = new ListNode(3, node4);
let node2 = new ListNode(2, node3);
let head1 = new ListNode(1, node2);
// Test 2: [1,2]
let nodeB = new ListNode(2);
let head2 = new ListNode(1, nodeB);
// Test 3: []
let head3 = null;
printList(reverse(head1));  // Output: [5,4,3,2,1]
printList(reverse(head2));  // Output: [2,1]
printList(reverse(head3));  // Output: []

// Best Approach: Iterative Approach
// Complexity Analysis:
// Time Complexity: O(n), where n is the number of nodes in the linked list.
// Space Complexity: O(1), as we are using only a constant amount of extra space.