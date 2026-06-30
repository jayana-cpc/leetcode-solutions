class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, used):
            if i == len(nums):
                res.append(used[:])
                return
            else:
                # use i
                used.append(nums[i])
                backtrack(i+1, used)
                used.pop()

                # skip i
                prev = nums[i]
                while i + 1 < len(nums) and nums[i] == nums[i+1]:
                    i += 1
                backtrack(i+1, used)
        backtrack(0, [])
        return res