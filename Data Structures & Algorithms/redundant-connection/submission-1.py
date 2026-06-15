class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        roots = list(range(len(edges) + 1)) # initially set the parent of eveery node to itself

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

        for x, y in edges:
            if not union(x, y):
                return [x, y]
