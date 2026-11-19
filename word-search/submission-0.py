class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()
        def dfs(r, c, word):
            visited.add((r, c))
            if len(word) <= 1:
                return True

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc

                if (
                    (new_r, new_c) not in visited and
                    -1 < new_r < m and
                    -1 < new_c < n and 
                    board[new_r][new_c] == word[1]
                ):
                    if dfs(new_r, new_c, word[1:]):
                        return True
            visited.remove((r, c))
            return False
        
        for r in range(m):
            for c in range(n):
                if (
                    (r, c) not in visited and 
                    board[r][c] == word[0] and 
                    dfs(r, c, word)
                    ):
                        return True
        return False


