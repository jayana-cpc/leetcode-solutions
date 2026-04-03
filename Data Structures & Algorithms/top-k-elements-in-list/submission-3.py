class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for i in nums:
            if i in hm.keys():
                hm[i] += 1
            else:
                hm[i] = 0
        res = []
        for value, count in hm.items():
            res.append([count, value])
        res.sort()
        ret = []
        i = len(res) - 1
        while k > 0:
            ret.append(res[i][1])
            i -= 1
            k -= 1
        return ret

      
                
        