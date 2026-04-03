class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set()
        for item in nums:
            num_set.add(item)
        gbl_count = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in num_set:
                lcl_count = 0
                count = 1
                while nums[i] + count in num_set:
                    lcl_count += 1
                    count += 1
                gbl_count = max(lcl_count, gbl_count)
        return gbl_count + 1
