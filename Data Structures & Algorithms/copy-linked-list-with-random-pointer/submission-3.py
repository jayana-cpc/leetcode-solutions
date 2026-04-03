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
        nodes = []
        ndict = {}
        size = 1
        while curr:
            nodes.append((curr.val, curr.next, curr.random, curr))
            curr = curr.next
            size += 1
        if size == 1:
            return None
        prev = None
        # 3 -> 7 -> 4 -> 5
        for i in range(len(nodes)):
            nxt = Node(nodes[i][0])
            if i != 0:
                prev.next = nxt
                prev = prev.next
            else:
                prev = nxt
                h = prev
            ndict[nodes[i][3]] = prev
            print(i)
        prev.next = None
        """
        {
            old: new
        }
        """
        curr = h
        for node in nodes:
            if not node[2]:
                curr.random = None
            else:
                curr.random = ndict.get(node[2], None)
            curr = curr.next
        return h



        

