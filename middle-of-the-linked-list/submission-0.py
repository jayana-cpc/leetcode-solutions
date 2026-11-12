# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        current = head
        while current != None:
            count += 1
            current = current.next
        
        newCount = 0
        current = head
        for i in range(count):
            if newCount == (count//2): #3
                return current
            newCount += 1    
            current = current.next
            


        