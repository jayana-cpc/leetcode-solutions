class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}

        for index, num in enumerate(nums):
            if num in hm:
                if abs(index - hm[num]) <= k:
                    return True
            hm[num] = index
        return False
