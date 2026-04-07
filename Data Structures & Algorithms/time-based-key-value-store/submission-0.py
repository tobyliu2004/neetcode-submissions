class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        whole = self.map[key]
        l = 0
        r = len(whole) - 1
        result = ""
        while l <= r:
            m = (l + r) // 2
            if whole[m][0] <= timestamp:
                result =  whole[m][1]
                l = m + 1
            else:
                r = m - 1
        return result
            