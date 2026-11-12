# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = head
        s = head

        while s and f.next:
            s = s.next
            f = f.next.next
            if not f or not s:
                return False
            if f == s:
                return True
        return False