class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for a in range(len(nums) - 1):
            if nums[a] > 0:
                break
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            b = a + 1
            c = len(nums) - 1
            while b < c:
                if nums[a] + nums[b] + nums[c] == 0:
                    res.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while nums[b] == nums[b - 1] and b < c:
                        b += 1
                elif nums[a] + nums[b] + nums[c] > 0:
                    c -= 1
                else:
                    b += 1
        return res




