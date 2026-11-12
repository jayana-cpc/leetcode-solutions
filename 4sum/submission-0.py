class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        p1 = 0
        p2 = 1
        p3 = 2
        p4 = len(nums) - 1
        nums.sort()
        res = []
        while p1 < len(nums) - 2:
            while p2 < len(nums) - 1:
                while p3 < p4:
                    sum = nums[p1] + nums[p2] + nums[p3] + nums[p4]
                    if sum == target and [nums[p1],nums[p2],nums[p3],nums[p4]] not in res:
                        res.append([nums[p1],nums[p2],nums[p3],nums[p4]])
                    elif sum > target:
                        p4 -= 1
                    elif sum < target:
                        p3 += 1
                    else: 
                        p3 += 1
                p2 += 1
                p4 = len(nums) - 1
                p3 = p2 + 1
            p1 += 1
            p2 = p1 + 1
            p4 = len(nums) - 1
            p3 = p2 + 1   
        return res



