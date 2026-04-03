# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid point
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next

        # reverse
        cur = mid
        prev = None
        slow.next = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # reorder
        tail = prev # 5
        cur = head # 1
        while tail:
            nxt = cur.next # 2
            nxt2 = tail.next # 4
            cur.next = tail # 0 -> 6
            tail.next = nxt
            cur = nxt 
            tail = nxt2 
        


