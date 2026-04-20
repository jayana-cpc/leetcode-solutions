class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        res = [intervals[0]]
        mini = 0
        for interval in intervals[1:]:
            if interval[0] >= res[-1][1]:
                res.append(interval)
            else:
                mini += 1
        return mini


