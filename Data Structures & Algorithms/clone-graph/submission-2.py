"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visited = {}
       
        def dfs(node, visited):
            if node in visited:
                return visited[node]
        
            copy = Node(node.val)
            visited[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor, visited))
            
            return copy
        if not node:
            return None
        root = dfs(node, visited)

        return root