class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.add((i, j))
                if grid[i][j] == 1:
                    count += 1
        
        q = list(rotten)
        
        time = 0

        while q and count:
            rotted = len(q)
            for _ in range(rotted):
                curr = q.pop(0)
                x = curr[0]
                y = curr[1]
                
                neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for neighbor in neighbors:
                    x2 = x + neighbor[0]
                    y2 = y + neighbor[1]

                    if x2 in range(0, len(grid)) and y2 in range(0, len(grid[0])) and grid[x2][y2] == 1:
                        q.append((x2, y2))
                        grid[x2][y2] = 2
                        count -= 1

            time += 1
        if not count:
            return time
        return -1
                
