class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0]*numCourses

        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        order = []
        q = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        while q:
            node = q.popleft()
            order.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return order if len(order) == numCourses else []

