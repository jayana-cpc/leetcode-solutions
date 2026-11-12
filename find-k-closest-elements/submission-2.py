class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        for index in range(len(arr)):
            arr[index] = (abs(x - arr[index]), arr[index])
        
        arr = sorted(arr)
        res = []
        for i in range(k):
            res.append(arr[i][1])

        return sorted(res)
