# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        first = head
        if not head:
            return head
        second = head.next
        if not (first and second):
            return head
        prvFirst = None
        head = second
        while first and second:
            nxtFirst = first.next
            nxtSecond = second.next
            if prvFirst:
                prvFirst.next = second
            second.next = first
            first.next = nxtSecond

            prvFirst = first

            first = first.next
            if first:
                second = first.next
        return head

