class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        def search(r, c):
            q = [(r, c)]
            visited.add((r, c))
            while q:
                r, c = q.pop(0)
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for x, y in directions:
                    if r+x in range(ROWS) and c+y in range(COLS) and grid[r+x][c+y] == "1" and (r+x, c+y) not in visited:
                        visited.add((r+x, c+y))
                        q.append((r+x, c+y))

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    search(r, c)
                    islands += 1
        return islands
        