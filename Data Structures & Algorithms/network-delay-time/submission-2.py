class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((w, v))
        
        minHeap = [(0, k)]
        time = 0
        visited = set()

        while minHeap:
            w, u = heapq.heappop(minHeap)

            if u in visited:
                continue
            visited.add(u)

            time = w

            for w2, v in edges[u]:
                if v not in visited:
                    heapq.heappush(minHeap, (w+w2, v))
        return time if len(visited) == n else -1