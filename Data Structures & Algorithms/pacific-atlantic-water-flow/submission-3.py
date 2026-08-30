from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = deque()
        pac = set()
        for i in range(len(heights[0])):
            pacific.append((0,i))
            pac.add((0,i))
        for i in range(1, len(heights)):
            pacific.append((i,0))
            pac.add((i,0))

        while pacific:
            for _ in range(len(pacific)):
                node = pacific.popleft()
                old = heights[node[0]][node[1]]
                

                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for dx, dy in directions:
                    new = (node[0]+dx,node[1]+dy)

                    if (
                        new not in pac
                        and new[0] in range(len(heights))
                        and new[1] in range(len(heights[0]))
                        and heights[new[0]][new[1]] >= old 
                    ):
                        pacific.append(new)
                        pac.add(new)
        atl = set()
        atlantic = deque()
        for i in range(len(heights[0])):
            atlantic.append((len(heights) - 1, i))
            atl.add((len(heights) - 1, i))

        for i in range(len(heights) - 1):
            atlantic.append((i, len(heights[0]) - 1))
            atl.add((i, len(heights[0]) - 1))
        while atlantic:
            for _ in range(len(atlantic)):
                node = atlantic.popleft()
                old = heights[node[0]][node[1]]
                

                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for dx, dy in directions:
                    new = (node[0]+dx,node[1]+dy)

                    if (
                        new not in atl
                        and new[0] in range(len(heights))
                        and new[1] in range(len(heights[0]))
                        and heights[new[0]][new[1]] >= old 
                    ):
                        atlantic.append(new)
                        atl.add(new)
        return [[r, c] for r, c in pac.intersection(atl)]



