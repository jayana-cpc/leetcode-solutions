# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        curr = ListNode()
        head = curr
        carry = 0
        while l1 or l2:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            if total > 9:
                total -= 10
                carry = 1
            else:
                carry = 0
            
            curr.next = ListNode(total)
            curr = curr.next
        if carry:
            curr.next = ListNode(1)
        return head.next

    