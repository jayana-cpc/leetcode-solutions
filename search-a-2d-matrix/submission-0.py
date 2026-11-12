class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        combined = []
        left = 0
        for x in matrix:
            combined.extend(x)
        right = len(combined) - 1
        while left <= right:
            middle = (left + right) // 2
            if combined[middle] < target:
                left = middle + 1
            elif combined[middle] > target:
                right = middle - 1
            elif combined[middle] == target:
                return True
        return False