class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, path, used):
            if len(used) == len(nums):
                res.append(list(path))
                return
            else:
                for x in nums:
                    if x not in used:
                        used.add(x)
                        path.append(x)
                        backtrack(i, path, used)
                        used.remove(x)
                        path.pop()
        backtrack(0, [], set())
        return res