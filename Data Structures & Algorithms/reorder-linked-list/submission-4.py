# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        f = head
        s = head

        while f and f.next:
            s = s.next
            f = f.next.next
        
        mid = s
        curr = mid
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        tail = prev
        curr = head
        # 2 -> 8 -> 4 -> 6
        while tail and curr.next:
            nxt = curr.next # 6
            curr.next = tail
            tail = tail.next # 6
            curr = curr.next # 8
            if nxt != curr:
                curr.next = nxt # 4
                curr = curr.next #4

        