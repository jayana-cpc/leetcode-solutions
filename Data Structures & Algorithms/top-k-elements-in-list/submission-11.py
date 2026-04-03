class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Here we get the frequency of each number in the array
        counts = Counter(nums)
        
        # Bucket Sort
        freq = [[] for _ in range(len(nums)+1)]
        for val, count in counts.items():
            freq[count].append(val)
        
        # create list of top k frequent elements
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for element in freq[i]:
                res.append(element)
                if len(res) == k:
                    return res


        