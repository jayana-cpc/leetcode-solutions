class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        n = len(nums)
        res = []
        for key in hm:
            if hm[key] > int(n / 3):
                res.append(key)
        return res

        