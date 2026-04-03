# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        size1 = 0
        curr = l1

        while curr:
            curr = curr.next
            size1 += 1

        size2 = 0
        curr = l2
        while curr:
            curr = curr.next
            size2 += 1
        if size1 > size2:
            curr = l2
            while curr.next:
                curr = curr.next
            for _ in range(size1-size2):
                curr.next = ListNode(0)
                curr = curr.next
        if size2 > size1:
            curr = l1
            while curr.next:
                curr = curr.next
            for _ in range(size2-size1):
                curr.next = ListNode(0)
                curr = curr.next
        head = prev = ListNode()
        """
        curr -> 5
        """
        carry = 0
        """
        8 -> 9 -> 9 -> 9 -> 0 -> 0 ->
        """
        while l1 and l2: 
            tot = l1.val + l2.val + carry
            carry = 0
            if len(str(tot)) > 1:
                prev.next = ListNode(int(str(tot)[1])) 
                carry = int(str(tot)[0]) # 1
            else:
                prev.next = ListNode(tot)
            prev = prev.next
            l1 = l1.next
            l2 = l2.next
        if carry:
            prev.next = ListNode(carry) 
        return head.next


