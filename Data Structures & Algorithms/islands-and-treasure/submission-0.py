class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        treasure = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    treasure.add((r, c))
        
        q = list(treasure)
        
        steps = 1
        while q:
            treasures = len(q)
            for _ in range(treasures):
                r, c = q.pop(0)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for x, y in directions:
                    if r+x in range(ROWS) and c+y in range(COLS) and (grid[r+x][c+y] == 2147483647):
                        grid[r+x][c+y] = steps
                        q.append((r+x, c+y))
            steps += 1





