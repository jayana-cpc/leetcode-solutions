class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        def dfs(u, parent):
            visited[u] = True

            for neighbor in adj[u]:
                if not visited[neighbor]:
                    if dfs(neighbor, u):
                        return True
                elif neighbor != parent:
                    return True
            return False
        
        dfs(0, -1)

        return all(visited)