class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""
        arr = self.cache[key]

        l = 0
        r = len(arr)-1
        res = ""
        while l <= r:
            mid = (l+r)//2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] < timestamp:
                res = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res