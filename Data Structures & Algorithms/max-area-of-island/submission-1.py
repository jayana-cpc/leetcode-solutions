class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        big = 0
        def dfs(node):
            x, y = node
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return 0
            if node in visited or grid[x][y] == 0:
                return 0
            visited.add(node)
            res = 1
            res += dfs((node[0]+1, node[1]))
            res += dfs((node[0]-1, node[1]))
            res += dfs((node[0], node[1]+1))
            res += dfs((node[0], node[1]-1))
            print(res)
            return res
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                big = max(dfs((i, j)), big)
        return big