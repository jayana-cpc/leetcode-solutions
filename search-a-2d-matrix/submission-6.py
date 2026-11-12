class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS - 1
        row = -1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][-1] >= target:
                if matrix[m][0] <= target:
                    row = m
                    break
                else:
                    r = m - 1
            else:
                l = m + 1
        if row == -1:
            return False

        l, r = 0, COLS

        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False









