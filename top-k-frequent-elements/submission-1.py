class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        res = []
        for i in nums:
            if i in occ:
                occ[i]+=1
            else:
                occ[i] = 1
        for i in range(k):
            top = 0
            topI = 0
            for i in occ:
                if occ[i] > top:
                    top = occ[i]
                    topI = i
            res.append(topI) 
            del occ[topI]
        return res