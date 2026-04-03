class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] in row:
                    return False
                elif board[i][j].isdigit():
                    row.add(board[i][j])
        
        for i in range(9):
            column = set()
            for j in range(9):
                if board[j][i] in column:
                    return False
                elif board[j][i].isdigit():
                    column.add(board[j][i])

        squares = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] in squares.get((i//3, j//3), []):
                    return False
                elif board[i][j].isdigit():
                    if (i//3, j//3) in squares.keys():
                        squares[(i//3, j//3)].append(board[i][j])
                    else:
                        squares[(i//3, j//3)] = [board[i][j]]

        return True

