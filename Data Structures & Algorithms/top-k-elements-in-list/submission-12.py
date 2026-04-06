class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        heap = []
        for num in counts:
            heapq.heappush(heap, (-counts[num], num))
        res = []
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
