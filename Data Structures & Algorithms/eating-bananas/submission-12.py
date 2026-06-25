class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float("inf")
        r = max(piles)
        l = 1
        while l <= r:
            mid = (l+r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res

            