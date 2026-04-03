# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of linked list
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        stop = count - n
        if stop == 0:
            return head.next
        curr = head
        count = 0
        while curr:
            count += 1
            if count == stop:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
