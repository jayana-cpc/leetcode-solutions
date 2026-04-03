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
        self.hm = {None: None}
        
        def copy(node):
            if not node:
                return None
            self.hm[node] = Node(node.val)
            copy(node.next)
        
        def link(node):
            if not node:
                return None
            copy = self.hm[node]
            copy.next = self.hm[node.next]
            copy.random = self.hm[node.random]
            link(node.next)
        
        copy(head)
        link(head)
        return self.hm[head]
