class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        row = self.hm[key]
        if len(row) == 0:
            return ""

        l = 0
        r = len(row) - 1
        best = ""

        while l <= r:
            mid = (l + r) // 2

            if row[mid][1] == timestamp:
                return row[mid][0]
            elif row[mid][1] < timestamp:
                best = row[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return best



