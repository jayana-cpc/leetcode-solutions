class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        merged = False
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                intervals.insert(i, newInterval)
                merged = True
                break
            elif newInterval[0] in range(intervals[i][0], intervals[i][1] + 1) or intervals[i][0] in range(newInterval[0], newInterval[1] + 1):
                merged = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                intervals[i] = merged
                merged = True
                break
        if not merged:
            intervals.append(newInterval)
                
        i = 0
        while i < len(intervals) - 1:
            if intervals[i+1][0] in range(intervals[i][0], intervals[i][1] + 1):
                merged = [min(intervals[i][0], intervals[i+1][0]), max(intervals[i][1], intervals[i+1][1])]
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i, merged)
            else:
                i += 1
        
        return intervals


