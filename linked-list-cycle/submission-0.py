# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head

        while curr:
            if (curr.val, curr.next) in seen:
                return True
            else:
                seen.add((curr.val, curr.next))
            curr = curr.next
        return False