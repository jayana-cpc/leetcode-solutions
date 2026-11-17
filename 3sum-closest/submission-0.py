class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        best = None
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            while l < r:
                total = (nums[i] + nums[l] + nums[r])
                score = abs(total - target)
                if best is None or score < abs(best - target):
                    best = nums[i] + nums[l] + nums[r]
                if total > target:
                    r -= 1
                else:
                    l += 1
        return best


