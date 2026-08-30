class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen = set()

        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)

            for nei in adj[node]:
                dfs(nei)
        res = 0
        for node in range(n):
            if node not in seen:
                dfs(node)
                res += 1
        return res