class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            distance = ((point[0])**2 + (point[1])**2)**(0.5)
            heap.append((distance, point))
        
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for i in range(k)]