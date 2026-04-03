# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.cur = head
        self.prev = None
        while self.cur:
            nxt = self.cur.next
            self.cur.next = self.prev
            self.prev = self.cur
            self.cur = nxt
        return self.prev