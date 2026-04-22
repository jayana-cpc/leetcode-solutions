class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for num in nums:
            if len(heap) >= k:
                if num > heap[0]:
                    heapq.heappop(heap)
                else:
                    continue
            heapq.heappush(heap, num)
        return heap[0]