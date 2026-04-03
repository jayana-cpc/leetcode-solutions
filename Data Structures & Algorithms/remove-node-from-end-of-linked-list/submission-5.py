# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        
        rem = length - n
        
        if rem == 0:
            return head.next
        print(rem)
        count = 0
        curr = head
        while curr:
            count += 1
            print(count, rem)
            if count == rem:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
