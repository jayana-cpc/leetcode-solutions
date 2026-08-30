from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        seen = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    seen.add((i, j))
                if grid[i][j] == 1:
                    count += 1
        if count == 0:
            return 0
        time = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for dx, dy in directions:
                    new = (node[0]+dx, node[1]+dy)

                    if (
                        new not in seen
                        and new[0] in range(len(grid))
                        and new[1] in range(len(grid[0]))
                        and grid[new[0]][new[1]] == 1
                    ):
                        seen.add(new)
                        q.append(new)
                        grid[new[0]][new[1]] = 2
                        count -= 1
            time += 1
            if count == 0:
                return time
        return -1

                
        