class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minHeap = [(0, 0)]
        visited = set()
        cost = 0
        while minHeap and len(visited) < n:
            w, u = heapq.heappop(minHeap)
            if u in visited:
                continue
            visited.add(u)
            cost += w

            for v in range(n):
                if v not in visited:
                    c = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(minHeap, (c, v))
        return cost
