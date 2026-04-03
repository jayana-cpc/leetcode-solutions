class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            if nums[i] in hm.keys():
                hm[nums[i]] = [hm[nums[i]][0] + 1, nums[i]]
            else:
                hm[nums[i]] = [1, nums[i]]

        res = []
        temp = list(hm.values())
        temp.sort(reverse=True)
        while k > 0:
            res.append(temp[0][1])
            temp.pop(0)
            k -= 1
        return res
