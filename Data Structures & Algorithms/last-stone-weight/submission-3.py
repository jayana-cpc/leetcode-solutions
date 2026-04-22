class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)

            if s1 - s2 != 0:
                heapq.heappush(heap, -abs(s1 - s2))
        if heap:
            return -heap[0]
        return 0
        