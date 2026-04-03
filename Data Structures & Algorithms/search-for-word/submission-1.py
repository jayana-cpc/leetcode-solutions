class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def isValid(r, c):
            if r in range(len(board)) and c in range(len(board[0])):
                return True
            else:
                return False

        def search(r, c, board, word, visited):
            if not word:
                return True
            visited.add((r, c))
            if board[r][c] == word: return True
            if board[r][c] == word[0]:
                for x, y in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                    if isValid(r+x, c+y) and (r+x, c+y) not in visited:
                        vis_cop = visited.copy()
                        vis_cop.add((r+x, c+y))
                        if search(r+x, c+y, board, word[1:], vis_cop):
                            return True
                return False
            else:
                return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if search(r, c, board, word, set()):
                    return True
        return False

        
        