import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        heap = []
        for key in freqs.keys():
            heapq.heappush(heap, (freqs[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [tup[1] for tup in heap]

        
