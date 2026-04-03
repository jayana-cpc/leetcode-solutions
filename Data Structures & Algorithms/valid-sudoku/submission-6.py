class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_hm = set()
            for item in row:
                if item in row_hm and item != ".":
                    print(row_hm)
                    return False
                elif item != ".":
                    row_hm.add(item)
        
        for col in range(len(board)):
            col_hm = set()
            for row in range(len(board)):
                if board[row][col] in col_hm and board[row][col] != ".":
                    return False
                elif board[row][col] != ".":
                    col_hm.add(board[row][col])
        print(col_hm)
        squares = {}
        for i in range(9):
            squares[i] = set()

        for col in range(len(board)):
            for row in range(len(board)):
                if board[row][col] in squares[(row//3)*3 + (col//3)] and board[row][col] != ".":
                    return False
                elif board[row][col] != ".":
                    squares[(row//3)*3 + (col//3)].add(board[row][col])
        print(squares)
        return True


            
