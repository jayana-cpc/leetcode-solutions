class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [(0, (points[0][0], points[0][1]))]
        visited = set()
        mst_weight = 0

        while len(visited) < len(points):
            w, node = heapq.heappop(minHeap)
            x1, y1 = node

            if node in visited:
                continue

            visited.add(node)
            mst_weight += w

            for x2, y2 in points:
                if (x2, y2) not in visited:
                    heapq.heappush(minHeap, (abs(x1-x2)+abs(y1-y2), (x2, y2)))
        return mst_weight 
