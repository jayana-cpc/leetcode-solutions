class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        roots = [i for i in range(len(edges)+1)]

        def root(node):
            if roots[node] != node:
                roots[node] = root(roots[node])
            return roots[node]

        def union(u, v):
            ru = root(u)
            rv = root(v)

            if ru == rv:
                return False
            roots[rv] = ru
            return True
        
        for u, v in edges:
            
            if not union(u, v):
                return [u, v]
        