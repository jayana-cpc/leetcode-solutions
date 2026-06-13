class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, t in times:
            edges[u].append((v, t))
        
        minHeap = [(0, k)]
        visit = set()
        time = 0
        while minHeap:
            t, v = heapq.heappop(minHeap)

            if v in visit:
                continue
            
            visit.add(v)
            time = t

            for v2, t2 in edges[v]:
                if v2 not in visit:
                    heapq.heappush(minHeap, (t + t2, v2))
        return time if len(visit) == n else -1

