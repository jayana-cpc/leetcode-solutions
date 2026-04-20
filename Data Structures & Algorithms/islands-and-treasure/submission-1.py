class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        coords = set()
        # find treasure

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    coords.add((i, j))
        q = list(coords)
        distance = 0
        while q:
            treasures = len(q)
            for _ in range(treasures):
                
                curr = q.pop(0)
                x = curr[0]
                y = curr[1]
                grid[x][y] = min(distance, grid[x][y])
                neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                
                for neighbor in neighbors:
                    x2 = x + neighbor[0]
                    y2 = y + neighbor[1]

                    if x2 in range(0, len(grid)) and y2 in range(0, len(grid[0])) and grid[x2][y2] == 2147483647:
                        q.append((x2, y2))
            distance += 1

