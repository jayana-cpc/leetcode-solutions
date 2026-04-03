# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        head = dummy
        cur1 = list1
        cur2 = list2
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                nxt = cur1.next
                dummy.next = cur1
                cur1 = nxt
                dummy = dummy.next
                
            else:
                nxt = cur2.next
                dummy.next = cur2
                cur2 = nxt
                dummy = dummy.next
                
        if cur1: 
            dummy.next = cur1
        else: 
            dummy.next = cur2
        return head.next
                
