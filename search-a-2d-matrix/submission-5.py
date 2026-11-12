class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS - 1
        arr = []
        while l <= r:
            m = (l + r) // 2
            if matrix[m][-1] >= target:
                if matrix[m][0] <= target:
                    arr = matrix[m]
                    break
                else:  
                    r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
        
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2
            
            if arr[m] > target:
                r = m - 1
            elif arr[m] < target:
                l = m + 1
            else:
                return True
        return False
            
