import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        occur = {}
        for i in nums:
            if i in freq.keys():
                freq[i] = 1 + freq[i]
            else:
                freq[i] = 1  

        keys = list(freq.keys())
        values = list(freq.values())
        sorted_value_index = np.argsort(values)
        occur = {keys[i]: values[i] for i in sorted_value_index}

        result = []
        loop = 0
        for i in reversed(occur.keys()):
            if loop < k:
                result.append(i)
                loop += 1
            else:
                return result
        return result    
