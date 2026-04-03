class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        res = []
        for i in nums:
            if i in hm:
                hm[i] = (hm[i][0] + 1, i)
            else:
                hm[i] = (1, i)
        
        freqs = sorted(list(hm.values()))

        for i in range(k):
            res.append(freqs[-1][1])
            freqs.pop()
        return res


        