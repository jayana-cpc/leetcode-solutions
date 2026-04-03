# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = l1
        list2 = l2
        dummy = ListNode()
        curr = dummy
        carry = 0
        # 9 -> 9 -> 9
        # 9 -> 9 -> 9
        # 8 -> 9 -> 9 -> 1
        while l1 or l2:
            l1val = 0
            l2val = 0
            if l1:
                l1val = l1.val
            if l2:
                l2val = l2.val
            sum = l1val+l2val+carry
            curr.next = ListNode(sum%10)
            carry = sum//10
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next