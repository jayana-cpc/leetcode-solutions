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
        print(size)

        count = size - n + 1
        print(count)
        curr = head
        prev = None
        for i in range(count):
            if i == count - 1 and prev:
                prev.next = curr.next
                break
            if i == count - 1 and not prev and size == 1:
                head = None
            if i == count - 1 and not prev:
                head = curr.next

            prev = curr #2
            curr = curr.next #3
        return head
           



