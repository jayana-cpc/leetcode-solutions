class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = max(piles)
        rate = r
        while l <= r:
            k = (l + r)//2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/k)
            if hrs <= h:
                r = k - 1
                rate = min(k, rate)
            else:
                l = k + 1
        return rate
