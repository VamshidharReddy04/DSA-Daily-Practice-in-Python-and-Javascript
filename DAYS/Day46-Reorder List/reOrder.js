// Linked List- Reorder List(Leetcode 143)
// Given a singly linked list L: L0→L1→…→Ln-1→Ln, reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
// You may not modify the values in the list's nodes, only nodes itself may be changed.
// Example 1: Input: 1->2->3->4 Output: 1->4->2->3
// Example 2: Input: 1->2->3->4->5 Output: 1->5->2->4->3
// Different approach :
// 1. Brute Force - Time Complexity: O(n) Space Complexity: O(n)
// 2. Optimal Approach - Time Complexity: O(n) Space Complexity: O(1)
// Solution of Optimal Approach

function ListNode(val) {
    this.val = val;
    this.next = null;
}
function reOrderList(head){
    if(!head || !head.next) return head;
    // Step 1: Find the middle of the linked list
    let slow = head;
    let fast=head;
    while(fast && fast.next){
        slow=slow.next;
        fast=fast.next.next;
    }
    // Step 2: Reverse the second half of the linked list
    let prev=null;
    let curr=slow.next;
    while (curr){
        let next=curr.next;
        curr.next=prev;
        prev=curr;
        curr=next;
    }
    slow.next=null; // Split the list into two halves
    // Step 3: Merge the two halves
    let first=head;
    let second=prev;
    while(first && second){
        let temp=first.next;
        first.next=second;
        first=temp;
        temp=second.next;
        second.next=first;
        second=temp;
    }
    return head;
}
//Helper Function to print the linked list
function printLists(head){
    let curr;
    curr=head;
    let val=[];
    while(curr){
        val.push(curr.val);
        curr=curr.next;
    }
    console.log(val.join("->"));
}
// Test Case
let head1 = new ListNode(1);
head1.next = new ListNode(2);
head1.next.next = new ListNode(3);
head1.next.next.next = new ListNode(4);
head1.next.next.next.next = new ListNode(5);
printLists(reOrderList(head1)); // Output: 1->5->2->4->3

// OR Bulild List from Array and Test Case More than 5 nodes

// Helper function to build a linked list from an array
function buildList(arr) {
    if (arr.length === 0) return null;
    let head = new ListNode(arr[0]);
    let current = head;
    for (let i = 1; i < arr.length; i++) {
        current.next = new ListNode(arr[i]);
        current = current.next;
    }
    return head;
}
// Test Case
let head2 = buildList([1,2,3,4,5,6,7,8,9,10]);
printLists(reOrderList(head2)); // Output: 1->10->2->9->3->8->4->7->5->6

// Best Approach - Optimal Approach 
// Complexity Analysis - Time Complexity: O(n) Space Complexity: O(1)