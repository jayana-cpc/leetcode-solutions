class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        largest = 0
        def dfs(node):
            seen.add(node)
            area = 1
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for nei in directions:
                new = (node[0]+nei[0],node[1]+nei[1])

                if (
                    new not in seen
                    and new[0] in range(len(grid))
                    and new[1] in range(len(grid[0]))
                    and grid[new[0]][new[1]] == 1
                    ):
                    area += dfs(new)
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == 1:
                    largest = max(largest, dfs((i, j)))
        return largest

            