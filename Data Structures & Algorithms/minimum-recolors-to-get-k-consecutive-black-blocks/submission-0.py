class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counts = {}
        res = float("inf")
        l = 0

        for r in range(len(blocks)):
            counts[blocks[r]] = counts.get(blocks[r], 0) + 1
            while counts.get("W", 0) + counts.get("B", 0) > k:
                counts[blocks[l]] -= 1
                if counts[blocks[l]] == 0:
                    del counts[blocks[l]]
                l += 1
            if counts.get("W", 0) + counts.get("B", 0) == k:
                res = min(k - counts.get("B", 0), res)
        return res
