class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, word, seen):
            if len(word) <= 1:
                return True
            else:
                seen.add((i, j))
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for x, y in directions:
                    if (i+x, j+y) not in seen and i+x > -1 and i+x < len(board) and j+y > -1 and j+y < len(board[0]):
                        if board[i+x][j+y] == word[1]:
                            if dfs(i+x, j+y, word[1:], seen):
                                return True
                seen.remove((i, j))
                return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, word, set()):
                        return True
        return False