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
        hm = {None: None}

        curr = head
        while curr:
            hm[curr] = Node(curr.val)
            curr = curr.next
        
        for node in hm:
            if node:
                copy = hm[node]
                copy.next = hm[node.next]
                copy.random = hm[node.random]

        return hm[head]