class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshCount = 0
        q = []
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    freshCount += 1
        minutes = 0
        while freshCount and q:
            qLen = len(q)
            for _ in range(qLen):
                r, c = q.pop(0)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for x, y in directions:
                    if r + x in range(ROWS) and c + y in range(COLS) and grid[r+x][c+y] == 1:
                        grid[r+x][c+y] = 2
                        q.append((r+x, c+y))
                        freshCount -= 1
            minutes += 1
        return minutes if not freshCount else -1

