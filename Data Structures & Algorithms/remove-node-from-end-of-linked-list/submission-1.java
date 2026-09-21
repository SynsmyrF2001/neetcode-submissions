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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // One-Pass Two Pointer: Maintain two pointers (fast and slow) seperated by a gap of n nodes
        ListNode dummy = new ListNode(0, head); // Use dummy node pointing to head to handle edge cases like deleting the head itself
        ListNode fast = dummy;
        ListNode slow = dummy;

        for (int i = 0; i <= n; i++) {
            fast = fast.next; // Move fast by n + 1 steps from a dummy node so that when fast reaches null, slow is positioned directly before the target node to be deleted
        }

        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }

        slow.next = slow.next.next;
        return dummy.next;

    }
}
