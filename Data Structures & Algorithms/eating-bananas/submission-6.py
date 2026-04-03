import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        bestk = r
        while l <= r:
            k = (l + r)//2
            hrs = sum([math.ceil(pile/k) for pile in piles])

            if hrs > h:
                l = k + 1
            elif hrs <= h:
                r = k - 1
                bestk = min(bestk, k)

        return bestk
