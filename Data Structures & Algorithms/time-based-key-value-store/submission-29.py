class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap or not self.timemap[key]:
            return ""
        temp = self.timemap[key]
        l = 0
        r = len(temp)-1
        res = ""
        while l <= r:
            mid = (l+r)//2
            if temp[mid][1] == timestamp:
                res = temp[mid][0]
                return res
            elif temp[mid][1] < timestamp:
                res = temp[mid][0]
                l = mid + 1
            else:
                r = mid - 1
            
        return res