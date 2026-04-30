class TimeMap:

    def __init__(self):
        self.base = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.base:
            self.base[key] = []
        self.base[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.base:
            return ""
        arr = self.base[key]
        l = 0
        r = len(arr)-1
        res = ""
        while l <= r:
            mid = (l+r) // 2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] < timestamp:
                res = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res