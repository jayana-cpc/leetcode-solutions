# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
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

        while tail and curr.next: 
            hxt = curr.next 
            curr.next = tail
            tail = tail.next
            curr = curr.next
            if hxt != curr:
                curr.next = hxt
                curr = curr.next

            


        




        

        