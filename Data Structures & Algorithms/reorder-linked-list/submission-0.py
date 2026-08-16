# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        
        # 1. Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half of the list
        prev = None 
        curr = slow 
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second_half_head = prev

        # 3. Merge the two halves 
        first_half_head = head
        while second_half_head.next:
            temp1 = first_half_head.next
            temp2 = second_half_head.next
            # Stop when second_half has only one node left
             
        
            first_half_head.next = second_half_head
            second_half_head.next = temp1
            
            first_half_head = temp1
            second_half_head = temp2
        