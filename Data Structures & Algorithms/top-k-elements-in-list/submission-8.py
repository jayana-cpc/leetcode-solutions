class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for i in nums:
            if i in hm:
                hm[i] = (hm[i][0] + 1, i)
            else:
                hm[i] = (1, i)
        
        e = list(hm.values())
        e.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(e[i][1])
        return res



        