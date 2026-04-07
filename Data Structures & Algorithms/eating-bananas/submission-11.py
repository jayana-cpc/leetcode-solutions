class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        best_k = r

        while l <= r:
            rate = (l+r)//2
            cur_h = 0

            for pile in piles:
                cur_h += math.ceil(pile/rate)
            if cur_h <= h:
                best_k = rate
                r = rate - 1
            else:
                l = rate + 1
            print(l, r)
        return best_k




