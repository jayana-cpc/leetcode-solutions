class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, total, used):
            if total == target:
                res.append(used[:])
                return
            elif total > target or i > len(nums) - 1:
                return
            else:
                # use i and use it again
                used.append(nums[i])
                backtrack(i, total + nums[i], used)
                used.pop()

                # use i and dont use it again
                # used.append(nums[i])
                # backtrack(i + 1, total + nums[i], used)
                # used.pop()
                
                # dont use i
                backtrack(i + 1, total, used)
        backtrack(0, 0, [])
        return list(res)

