class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r, c) not in visit and r in range(ROWS) and c in range(COLS) and heights[r][c] >= prevHeight:
                visit.add((r, c))
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for x, y in directions:
                    dfs(r+x, c+y, visit, heights[r][c])


        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

        