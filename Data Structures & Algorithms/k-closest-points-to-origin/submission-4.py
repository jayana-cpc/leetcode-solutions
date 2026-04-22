class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)


        for point in points:
            distance = ((point[0])**2 + (point[1])**2)**0.5
            if len(heap) >= k:
                if distance < -heap[0][0]:
                    heapq.heappop(heap)
                else:
                    continue
            heapq.heappush(heap, (-distance, point))
        return [item[1] for item in heap]
        
        
