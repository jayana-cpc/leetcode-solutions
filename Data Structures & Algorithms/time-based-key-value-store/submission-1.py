class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        search = self.hm[key]
        curr = ""
        l = 0
        r = len(search) - 1
        while l <= r:
            mid = (l + r)//2
            if search[mid][0] <= timestamp:
                curr = search[mid][1]
                l = mid + 1
            elif search[mid][0] > timestamp:
                r = mid - 1
        return curr