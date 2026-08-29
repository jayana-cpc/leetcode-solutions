class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        def dfs(node):
            seen.add(node)
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for nei in directions:
                dx, dy = nei
                if (
                    (node[0]+dx,node[1]+dy) not in seen
                    and node[0]+dx in range(len(grid))
                    and node[1]+dy in range(len(grid[0]))
                    and grid[node[0]+dx][node[1]+dy] == '1'
                    ):
                    
                    dfs((node[0]+dx, node[1]+dy))
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == '1':
                    dfs((i, j))
                    count += 1
        return count
