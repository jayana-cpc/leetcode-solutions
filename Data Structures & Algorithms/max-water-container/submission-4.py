class Solution:
    def maxArea(self, heights: List[int]) -> int:
        topVolume = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            volume = min(heights[left], heights[right]) * (right - left)

            if volume > topVolume:
                topVolume = volume

            if heights[left] > heights[right]:
                right -=1
            # elif heights[left] < heights[right]:
            else:
                left += 1
    
        return topVolume