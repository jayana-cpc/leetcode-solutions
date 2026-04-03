# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def add(list1, list2, carry):
            if not list1 and not list2 and not carry:
                return None
            l1val = list1.val if list1 else 0
            l2val = list2.val if list2 else 0

            sum = l1val + l2val + carry
            carry = sum//10
            val = sum%10
            
            l1next = list1.next if list1 else None
            l2next = list2.next if list2 else None
            return ListNode(val, add(l1next, l2next, carry))
        
        return add(l1, l2, 0)
