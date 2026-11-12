class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for num in nums:
            if num in hm:
                hm[num] = (hm[num][0] + 1, num)
            else:
                hm[num] = (1, num)
        la = list(hm.values())
        la.sort()
        la.reverse()
        res = []
        print(la)
        for i in range(k):
            res.append(la[i][1])
        return res
