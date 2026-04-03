class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def bfs(r, c):
            q = [(r, c)]
            visited.add((r, c))
            while q:
                node = q.pop()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dx, dy in directions:
                    new_x, new_y = node[0]+dx, node[1]+dy
                    if new_x in range(ROWS) and new_y in range(COLS) and (new_x, new_y) not in visited and grid[new_x][new_y] == "1":
                        visited.add((new_x, new_y)) 
                        q.append((new_x, new_y))


        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
        return count


        