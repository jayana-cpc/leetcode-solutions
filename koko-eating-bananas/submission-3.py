import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = float('inf')

        while l <= r:
            m = (l + r) // 2
            hs = h
            for pile in piles:
                hs -= math.ceil(pile / m)
            if hs < 0:
                l = m + 1
            else:
                best = min(best, m)
                r = m - 1
        
        return best



