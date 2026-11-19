class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for r in range(len(matrix)):
            for c in range(r, len(matrix)):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for row in matrix:
            row.reverse()