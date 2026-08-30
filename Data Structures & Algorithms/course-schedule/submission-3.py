class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0]*numCourses

        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        processed = 0

        q = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        while q:
            node = q.popleft()
            processed += 1
            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
        return processed == numCourses

