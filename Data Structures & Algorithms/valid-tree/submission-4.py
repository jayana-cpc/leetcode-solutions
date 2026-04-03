class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if you visit a node and it has already been visited && it is not the parent
        # of the start node. 
        if len(edges) != (n - 1):
            return False
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False]*len(adj)
        def dfs(u, parent):
            visited[u] = True

            for v in adj[u]:
                if not visited[v]:
                    if dfs(v, u):
                        return True
                elif v != parent:
                    return True
            return False

        
        if dfs(0, -1):
            return False

        return all(visited)



        