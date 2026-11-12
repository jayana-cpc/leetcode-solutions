import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        p = max(piles)
        l = 1
        r = p + 1
        best = 1000000000000
        while l <= r:
            m = (l + r) // 2
            hs = h
            for pile in piles:
                hs -= math.ceil(pile / m)
            if hs >= 0:
                best = min(best, m)
                r = m - 1
            else:
                l = m + 1
            
        return best