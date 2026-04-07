class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find row

        t = 0
        b = len(matrix) - 1
        r = -1

        while t <= b:
            m=(t+b)//2

            if target >= matrix[m][0] and target <= matrix[m][-1]:
                r = m
                break
            elif target > matrix[m][-1]:
                t = m + 1
            else:
                b = m - 1
        if r == -1: return False

        aray = matrix[r]

        l = 0
        r = len(aray) - 1

        while l <= r:
            m = (l+r)//2

            if target == aray[m]:
                return True
            elif target > aray[m]:
                l = m + 1
            else:
                r = m - 1
        return False
