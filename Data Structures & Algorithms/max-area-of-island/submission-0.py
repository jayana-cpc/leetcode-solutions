class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        def search(r, c):
            size = 1
            q = [(r, c)]
            visited.add((r, c))
            while q:
                r, c = q.pop(0)
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for x, y in directions:
                    if r+x in range(ROWS) and c+y in range(COLS) and grid[r+x][c+y] == 1 and (r+x, c+y) not in visited:
                        visited.add((r+x, c+y))
                        q.append((r+x, c+y))
                        size += 1
            return size

        best = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    
                    size = search(r, c)
                    best = max(best, size)
        return best
        