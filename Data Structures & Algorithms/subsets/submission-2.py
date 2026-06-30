class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, used):
            if i > len(nums) - 1:
                add = list(used)
                res.append(add)
                return
            else:
                # use i
                used.append(nums[i])
                dfs(i+1, used)
                used.remove(nums[i])

                # skip i
                dfs(i+1, used)
        dfs(0, [])
        return res
