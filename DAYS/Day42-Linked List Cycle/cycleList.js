// Linked List- Linked List Cycle
// Type of Problem: linked list, Cycle detection(Two Pointer Approach/hashing)
// Given head, the head of a linked list, determine if the linked list has a cycle in it.
// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
// Example 1: Input: head = [3,2,0,-4], Output: true
// Example 2: Input: head = [1,2], Output: true
// Example 3: Input: head = [1], Output: false

// Different Approaches:
// 1. Hashing / Set Approach - Time Complexity: O(n), Space Complexity: O(n)
// 2. Two Pointer Approach - Time Complexity: O(n), Space Complexity: O(1)
// 3. Floyd’s Cycle-Finding Algorithm - Time Complexity: O(n), Space Complexity: O(1)
// 4. Modifying the Linked List - Time Complexity: O(n), Space Complexity: O(1) (Not Recommended)

class ListNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}
function cycleList(head){
    let slow=head;
    let fast=head;
    while(fast && fast.next){
        slow=slow.next;
        fast=fast.next.next;
        if(slow===fast) return true;
    }
    return false
}

// Test Cases
let head1 = new ListNode(3);
head1.next = new ListNode(2);
head1.next.next = new ListNode(0);
head1.next.next.next = new ListNode(-4);
head1.next.next.next.next = head1.next; // Creates a cycle
console.log(cycleList(head1)); // Output: true
let head2 = new ListNode(1);
head2.next = new ListNode(2);
head2.next.next = head2; // Creates a cycle
console.log(cycleList(head2)); // Output: true
let head3 = new ListNode(1);
console.log(cycleList(head3)); // Output: false