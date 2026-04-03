class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = len(heights) - 1
        maxV = 0
        while a < b:
            volume = min(heights[a], heights[b]) * (b - a)
            if volume > maxV:
                maxV = volume
            if heights[a] < heights[b]:
                a+=1
            else:
                b-=1
                
        return maxV




        