# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            som = num1 + num2 + carry
            if som > 9:
                carry = 1
                curr.next = ListNode(som%10)
            else:
                carry = 0
                curr.next = ListNode(som)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        if carry:
            curr.next = ListNode(1)
        
        return dummy.next
            

            
