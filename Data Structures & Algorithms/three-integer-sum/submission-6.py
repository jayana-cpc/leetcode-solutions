class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while l < r and l > i and r < len(nums):
                print([nums[i], nums[l], nums[r]])
                if nums[i] + nums[l] + nums[r] == 0:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return res