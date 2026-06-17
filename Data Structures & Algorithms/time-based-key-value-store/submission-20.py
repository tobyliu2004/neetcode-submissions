class TimeMap:

    def __init__(self):
        self.case = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.case:    
            self.case[key] = []
        self.case[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.case or not self.case[key]:
            return ""
        temp = self.case[key]
        l = 0
        r = len(temp)-1
        while l <= r:
            mid = (l+r)//2
            if temp[mid][0] == timestamp:
                return temp[mid][1]
            elif temp[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        if r >= 0:
            return temp[r][1]
        else:
            return ""