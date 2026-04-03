# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add = ListNode()
        head = add
        carry = 0
        while l1 or l2:
            first, second = 0,0
            if l1:
                first = l1.val
                l1 = l1.next
            if l2:
                second = l2.val
                l2 = l2.next
            total = first + second + carry
            if len(str(total))>1:
                add.next = ListNode(int(str(total)[1]))
                carry = 1
            else:
                add.next = ListNode(total)
                carry = 0
            add = add.next
        if carry: add.next = ListNode(carry)
        return head.next


