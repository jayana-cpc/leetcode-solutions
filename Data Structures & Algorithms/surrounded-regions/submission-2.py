from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        border = set()
        seen = set()
        safe = set()
        m = len(board)
        n = len(board[0])
        for c in range(n):
            if board[0][c] == 'O':
                border.add((0, c))
                safe.add((0, c))
            if board[m-1][c] == 'O':
                border.add((m - 1, c))
                safe.add((m - 1, c))
            seen.add((0, c))
            seen.add((m - 1, c))
        for r in range(m):
            if board[r][0] == 'O':
                border.add((r, 0))
                safe.add((r, 0))
            if board[r][n-1] == 'O':
                border.add((r, n - 1))
                safe.add((r, n - 1))
            seen.add((r, 0))
            seen.add((r, n - 1))
        border = deque(border)
        
        print(border)
        while border:
            for _ in range(len(border)):
                node = border.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dx, dy in directions:
                    new = (node[0]+dx, node[1]+dy)
                    if (
                        new not in seen
                        and new[0] in range(len(board))
                        and new[1] in range(len(board[0]))
                        and board[new[0]][new[1]] == 'O'
                    ):
                        
                        safe.add(new)
                        seen.add(new)
                        border.append(new)
        print(safe)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i,j) not in safe:
                    board[i][j] = 'X'



        

        
