# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid point
        f = head
        s = head

        while s and f and f.next:
            f = f.next.next
            s = s.next
        
        mid = s.next
        curr = mid
        prev = s.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # reorder
        tail = prev
        curr = head

        while tail:
            t1, t2 = curr.next, tail.next
            curr.next = tail
            tail.next = t1
            curr, tail = t1, t2
        


            