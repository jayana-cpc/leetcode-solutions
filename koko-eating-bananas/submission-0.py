import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        H = h #-1
        ks = []
        l = 1
        r = k
        while l <= r:
            k = (l + r) // 2
            for pile in piles:
                hc = math.ceil(pile/k)
                H -= hc
            if H > 0:
                r = k - 1
                ks.append(k)
            elif H < 0:
                l = k + 1
            else:
                ks.append(k)
                r = k - 1
            H = h

        return min(ks)



        # for k in range(1, k+1):
        #     for pile in piles:
        #         hc = math.ceil(pile/k)
        #         H -= hc
        #     if H >= 0:
        #         return k
        # return k  