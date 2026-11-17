# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        first, second = head, head.next
        nxtSecond = second.next
        second.next = first
        first.next = self.swapPairs(nxtSecond)
        return second
