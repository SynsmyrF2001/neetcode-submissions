/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        // Pointer Manipulation: Each node only knows about next in a singly linked list, in a reverse node A -> B must become B -> A
        // State Tracking: Changing curr.next breaks the forward traversal, a temporary pointer should store curr.next before overwriting
        // 3 Pointer Tech: Keep prev(init. null), curr(init. head), and nextTemp to iteratively reverse pointers in a single pass w/o extra mem.
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null){
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }

        return prev;
        
    }
}
