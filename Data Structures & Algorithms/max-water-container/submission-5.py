class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l = 0
        r = len(heights) - 1
        while l < r and l > -1 and r < len(heights):
            best = max(min(heights[l], heights[r]) * (r - l), best)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best