class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)
        counts = [[] for _ in range(len(nums)+1)]
        for num, count in hm.items():
            counts[count].append(num)
        res = []
        for i in range(len(counts)-1, 0, -1):
            for num in counts[i]:
                res.append(num)
                if len(res) == k:
                    return res


        
        
        