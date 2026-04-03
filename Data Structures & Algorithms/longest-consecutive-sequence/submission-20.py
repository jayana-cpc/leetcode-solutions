class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        gbl_count = 0
        for num in nums:
            if num - 1 not in elements:
                lcl_count = 1
                while num + lcl_count in elements:
                    lcl_count += 1
                gbl_count = max(gbl_count, lcl_count)
        return gbl_count

