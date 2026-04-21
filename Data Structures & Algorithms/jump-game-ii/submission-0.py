class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Greedy Choicee:
        We are always choosing the index that will give us
        the MOST OPTIONS or FARTHEST JUMP in the NEXT JUMP.
        """
        res = l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res

