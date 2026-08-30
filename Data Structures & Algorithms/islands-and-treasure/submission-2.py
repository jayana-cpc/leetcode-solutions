from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi source BFS

        q = deque()
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
                    seen.add((i, j))
        dist = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                grid[node[0]][node[1]] = dist

                directions = [(0,1), (0,-1), (1,0), (-1,0)]

                for dx, dy in directions:
                    new = (node[0]+dx, node[1]+dy)

                    if (
                        new not in seen
                        and new[0] in range(len(grid))
                        and new[1] in range(len(grid[0]))
                        and grid[new[0]][new[1]] != -1
                    ):
                        seen.add(new)
                        q.append(new)
            dist += 1



