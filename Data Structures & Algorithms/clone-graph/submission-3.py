"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        ogToClone = {}
        def dfs(node):
            if not node:
                return None
            if node in ogToClone:
                return ogToClone[node]
            ogToClone[node] = Node(node.val)

            for nei in node.neighbors:
                ogToClone[node].neighbors.append(dfs(nei))
            return ogToClone[node]
        return dfs(node)
        
