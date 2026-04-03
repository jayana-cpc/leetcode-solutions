class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])

        def search(word, r, c, visited):
            if not word or board[r][c] == word:
                return True
            visited.add((r, c))
            if board[r][c] != word[0]:
                return False

            neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for x, y in neighbors:
                if r+x in range(ROW) and c+y in range(COL) and (r+x, c+y) not in visited:
                    visited.add((r+x, c+y))
                    if search(word[1:], r+x, c+y, visited):
                        return True
                    visited.remove((r+x, c+y))

            return False

        for r in range(ROW):
            for c in range(COL):
                if search(word, r, c, set()):
                    return True 
        return False




