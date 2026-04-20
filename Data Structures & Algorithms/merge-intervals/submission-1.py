class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        while i < len(intervals) - 1:
            if intervals[i+1][0] > intervals[i][1]:
                i += 1
                continue
            elif intervals[i][1] < intervals[i+1][0]:
                i += 1
                continue
            else:
                merged = [
                    min(intervals[i][0], intervals[i+1][0]),
                    max(intervals[i][1], intervals[i+1][1])
                ]
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i, merged)

        return intervals
