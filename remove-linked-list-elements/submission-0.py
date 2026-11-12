# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 1 > 2 > 2 > 1
        current = head
        previous = None
        while current != None:
            if current.val == val:
                current = current.next
                if previous == None:
                    head = current
                
            elif current.next == None:
                return head
            elif current.next.val == val:
                temp = current.next.next
                while temp != None and temp.val == val:
                    temp = temp.next

                current.next = temp
                previous = current
                current = current.next
            else:
                current = current.next

        return head
        
                


