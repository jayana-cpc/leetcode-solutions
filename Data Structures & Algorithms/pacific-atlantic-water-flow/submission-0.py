class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        def bfs(r, c):
            seen = set()
            pacific = False
            atlantic = False
            q = [(r, c)]
            seen.add((r, c))
            while q:
                l, f = q.pop(0)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for x, y in directions:
                    if l+x >= ROWS or f+y >= COLS:
                        atlantic = True
                    if l+x < 0 or f+y < 0:
                        pacific = True
                    if l+x in range(ROWS) and f+y in range(COLS) and (l+x, f+y) not in seen and heights[l][f] >= heights[l+x][f+y]:
                        seen.add((l+x, f+y))
                        q.append((l+x, f+y))

            return pacific and atlantic
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if bfs(r, c):
                    res.append([r, c])
        return res