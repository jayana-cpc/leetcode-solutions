class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)): #0,8
            for c in range(len(board)): #0,8 
                element = board[r][c]

                if element == ".":
                    continue
                
                if element in rows[r] or element in cols[c] or element in squares[(r//3,c//3)]:
                    return False
                rows[r].add(element)
                cols[c].add(element)
                squares[(r//3,c//3)].add(element)
        return True


