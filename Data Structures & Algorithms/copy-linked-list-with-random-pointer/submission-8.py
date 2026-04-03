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
        if not head:
            return None
        hm = {}

        curr = head
        while curr:
            hm[curr] = Node(curr.val)
            curr = curr.next
        
        for node in hm:
            copy = hm[node]
            if not node.next:
                copy.next = None
            else:
                copy.next = hm[node.next]
            if not node.random:
                copy.random = None
            else:    
                copy.random = hm[node.random]
        return hm[head]