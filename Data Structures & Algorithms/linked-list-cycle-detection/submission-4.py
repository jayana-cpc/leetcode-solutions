# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if head: fast = head.next
        while slow and fast and fast.next:
            if slow.val == fast.val:
                return True
            slow = slow.next
            fast = fast.next.next
        return False