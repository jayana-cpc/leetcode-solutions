class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        tups = []
        for num in arr:
            tups.append((abs(x - num), num))
        
        tups.sort()
        res = []
        for i in range(k):
            res.append(tups[i][1])

        return sorted(res)
