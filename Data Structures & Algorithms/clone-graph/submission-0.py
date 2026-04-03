"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(vertex):
            if not vertex:
                return
            oldToNew[vertex] = Node(vertex.val)
            for node in vertex.neighbors:
                if node not in oldToNew:
                    dfs(node)

        dfs(node)

        for old in oldToNew:
            new = oldToNew[old]
            new.neighbors = [oldToNew[vertex] for vertex in old.neighbors]
        return oldToNew[node] if node else None