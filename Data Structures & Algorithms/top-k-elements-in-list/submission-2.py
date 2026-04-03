class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = 0
        for i in sorted(nums,key=nums.count, reverse=True):
            if i not in result and count < k:
                result.append(i)
                count += 1
        return result
      
                
        