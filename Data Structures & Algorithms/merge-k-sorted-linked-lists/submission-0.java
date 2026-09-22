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
    public ListNode mergeKLists(ListNode[] lists) {
        // Brute Force Approach: Traverse every node across allf the k-th lists, collect their values in an array/list, sort the array, adn reconstruct a new linked list
        // Priority Queue (Min-Heap): Maintain a min-heap of size at most k containing the current node from each non-empty list. Repeatedly extract the minimum node, append it to the result, and push its nect node if present
        // Divide and Conquer (Merge Sort): Pair up lists and merge them two at a time using the standard merge two sorted list algorithm. This achieves optimal O(1) auxiliary space while matching the O(N\log K) time complexity
        if (lists == null || lists.length == 0) return null;
        int interval = 1;
        while (interval < lists.length) {
            for (int i = 0; i + interval < lists.length; i += interval * 2) {
                lists[i] = mergeTwoLists(lists[i], lists[i + interval]);
            }
            interval *= 2;
        }
        return lists[0];
    }

    // Merger Sort Algo Class
    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0), curr = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                curr.next = l1;
                l1 =l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        curr.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }
}
