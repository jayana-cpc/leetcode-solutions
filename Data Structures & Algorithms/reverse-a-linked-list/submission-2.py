# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        # [0,1,2]
        while curr:
            nxt = curr.next # 1
            curr.next = prev # None
            prev = curr
            curr = nxt
        return prev
