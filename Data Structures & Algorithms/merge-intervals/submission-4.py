class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] > res[-1][1]:
                res.append(interval)
                continue
            else:
                merged = [
                    min(interval[0], res[-1][0]),
                    max(interval[1], res[-1][1])
                ]
                print(merged)
                res.pop()
                res.append(merged)
        return res
