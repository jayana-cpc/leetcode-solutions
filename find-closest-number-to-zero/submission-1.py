class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        hm = {}

        for num in nums:
            diff = abs(num)
            if diff in hm:
                hm[diff].append(num)
            else:
                hm[diff] = [num]
        
        i = min(list(hm.keys()))
        return max(hm[i])

            
