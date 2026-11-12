# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head

        while curr:
            curr = curr.next
            size += 1
        
        count = size - n
        dummy = curr = ListNode()
        dummy.next = head
        curr = head
        # dummy -> 1 -> 2
        
        if count == 0:
            return head.next      
        for i in range(0, count + 1):
            
            if count == i + 1:
                curr.next = curr.next.next
            else: curr = curr.next
        return head

