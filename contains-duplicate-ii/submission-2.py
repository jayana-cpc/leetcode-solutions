class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        chars = set()
        i = 0

        for j in range(len(nums)):
            if abs(i - j) > k:
                chars.remove(nums[i])
                i += 1     
            if nums[j] in chars:
                return True
            chars.add(nums[j])
        return False
