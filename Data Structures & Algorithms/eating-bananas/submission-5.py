class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        H = h
        ks = k
        l = 1
        r = k
        while l <= r:
            k = (l + r) // 2
            for pile in piles:
                hc = math.ceil(pile/k)
                H -= hc
            if H >= 0:
                r = k - 1
                ks = min(ks, k)
            elif H < 0:
                l = k + 1
            H = h

        return ks 