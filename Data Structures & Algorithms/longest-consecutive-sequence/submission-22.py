class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums): return 0
        existence = set()
        for num in nums:
            existence.add(num)
        
        best = 1
        for num in existence:
            count = 1
            while num + count in existence:
                count += 1
            best = max(count, best)
        return best