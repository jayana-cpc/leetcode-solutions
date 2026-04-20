class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        curr = nums[0]

        for num in nums[1:]:
            curr = max(num, curr + num)
            best = max(best, curr)
        return best
            