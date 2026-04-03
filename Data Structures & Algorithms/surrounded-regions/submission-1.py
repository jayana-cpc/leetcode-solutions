class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS = len(board)
        COLS = len(board[0])
        zeroCount = 0
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    zeroCount += 1

        def bfs(r, c, visited):
            region = set()
            touchWater = False
            q = [(r, c)]
            region.add((r, c))
            while q:
                node = q.pop(0)
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for x, y in directions:
                    newR = node[0]+x
                    newC = node[1]+y
                    if newR not in range(ROWS) or newC not in range(COLS):
                        touchWater = True
                    if newR in range(ROWS) and newC in range(COLS) and (newR, newC) not in region and board[newR][newC] == "O":
                        region.add((newR, newC))
                        q.append((newR, newC))
            if len(region) <= zeroCount and not touchWater:
                for spot in region:
                    board[spot[0]][spot[1]] = "X"
            visited.union(region)


        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visited:
                    bfs(r, c, visited)
