
class TimeMap:

    def __init__(self):
        self.h = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.h:
            self.h[key] = []

        self.h[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.h:
            return ""

        arr = self.h[key]
        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            ts, value = arr[mid]

            if ts <= timestamp:
                res = value
                l = mid + 1
            else:
                r = mid - 1

        return res
