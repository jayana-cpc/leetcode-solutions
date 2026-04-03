# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        
        # find the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next

        # reverse the linked list
        curr = mid
        prev = None
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        tail = prev
        curr = head
        # dummy -> 0 -> 6
        while tail:
            nxt = curr.next
            tnxt = tail.next
            curr.next = tail
            tail.next = nxt
            curr = nxt
            tail = tnxt
            







