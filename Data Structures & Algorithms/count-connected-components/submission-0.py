class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(u, parent):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs(v, u)

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False]*len(adj)
        count = 0
        for v in range(len(adj)):
            if not visited[v]:
                dfs(v, -1)
                count += 1
        return count


            





