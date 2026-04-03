class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posD = set() # (r - c)
        negD = set() # (r + c)
        res = []
        board = [["."]*n for _ in range(n)]
        def backtrack(r, board):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c not in cols and (r - c) not in posD and (r + c) not in negD:
                    cols.add(c)
                    posD.add(r - c)
                    negD.add(r + c)
                    board[r][c] = "Q"
                    backtrack(r+1, board)
                    cols.remove(c)
                    posD.remove(r - c)
                    negD.remove(r + c)
                    board[r][c] = "."
        backtrack(0, board)
        return res
