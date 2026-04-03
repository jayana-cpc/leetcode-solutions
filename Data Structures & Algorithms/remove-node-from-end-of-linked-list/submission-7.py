# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        start = head
        end = head

        for _ in range(n):
            end = end.next
        if not end:
            return head.next
        
        while end and end.next:
            end = end.next
            start = start.next
        start.next = start.next.next
        return head
        

