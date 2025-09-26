// Linked List- Remove nth Node From End of List( leetcode 19)
// Given the head of a linked list, remove the nth node from the end of the list and return its head.
// Example 1: Input: head = [1,2,3,4,5], n = 2 Output: [1,2,3,5]
// Example 2: Input: head = [1], n = 1 Output: []
// Example 3: Input: head = [1,2], n = 1 Output: [1]
// Different Approaches:
// 1. Two Pass Solution -Time Complexity: O(n), Space Complexity: O(1)
// 2. One Pass Solution - Time Complexity: O(n), Space Complexity: O(1)
// Solution 1: Two Pass Solution

function ListNode(val, next) {
    this.val = val;
    this.next = next;
}
function removeNode(head,n){
    let dummy = new ListNode(0, head);
    let slow = dummy, fast = dummy;
    for (let i = 0; i < n + 1; i++) {
        fast = fast.next;
    }
    while (fast) {
        slow = slow.next;
        fast = fast.next;
    }
    slow.next = slow.next.next;
    return dummy.next;
}
// Helper function to create a linked list 
function consoleList(head) {
    let val=[]
    while(head){
        val.push(head.val)
        head=head.next
    }
    return val
}
// Test Cases
let heads=new ListNode(1,new ListNode(2,new ListNode(3,new ListNode(4,new ListNode(5)))))
let n=2
let newHead = removeNode(heads, n);
console.log(consoleList(newHead)); // Output: [1, 2, 3, 5]
let heads1=new ListNode(1)
let n1=1
let newHead1 = removeNode(heads1, n1);
console.log(consoleList(newHead1)); // Output: []
let heads2=new ListNode(1,new ListNode(2))
let n2=1    
let newHead2 = removeNode(heads2, n2);
console.log(consoleList(newHead2)); // Output: [1]
// Best Approach: One Pass Solution
// Complxity Analysis: Time Complexity: O(n), Space Complexity: O(1)

