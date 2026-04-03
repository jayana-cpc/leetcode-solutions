import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occur = {}

        for i in nums:
            if i in occur.keys():
                occur[i] += 1
            else:
                occur[i] = 1

        keys = list(occur.keys())
        vals = list(occur.values())
        ideal = np.argsort(vals)
        sortedOccur = {keys[i]: vals[i] for i in ideal}
        result = []
        times = k
        index = 0
        while times > 0:
            result.append(list(sortedOccur.keys())[len(sortedOccur.keys()) - 1 - index])
            times -= 1
            index += 1
        return result
    


        