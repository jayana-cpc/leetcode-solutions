class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        maj = int(len(nums) / 2)
        print(maj)
        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
                if hm[num] > maj: 
                    return num
            else:
                hm[num] = 1
        return res
        
