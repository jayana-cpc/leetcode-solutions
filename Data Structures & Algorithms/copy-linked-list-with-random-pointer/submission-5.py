"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        hm = {}
        while curr:
            new = Node(curr.val)
            hm[curr] = new
            curr = curr.next
        
        curr = head
        while curr:
            copy = hm[curr]
            copy.next = hm.get(curr.next, None)
            copy.random = hm.get(curr.random, None)
            curr = curr.next
        return hm.get(head, None)


        

            
        
