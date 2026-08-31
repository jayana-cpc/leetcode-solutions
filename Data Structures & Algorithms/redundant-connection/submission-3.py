class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        roots = [i for i in range(len(edges)+1)]

        def root(x):
            if roots[x] != x:
                roots[x] = root(roots[x])
            return roots[x]
        
        def union(x, y):
            rx = root(x)
            ry = root(y)

            if rx == ry:
                return False
            roots[ry] = rx
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]