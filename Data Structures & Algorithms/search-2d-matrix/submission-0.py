class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        full = matrix[0]
        for m in matrix[1:]:
            full.extend(m)
        l = 0
        r = len(full) - 1
        while l <= r:
            m = (l + r) // 2
            if full[m] == target:
                return True
            elif full[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
        

        