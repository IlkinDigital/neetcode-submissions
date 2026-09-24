class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key] = self.hmap.get(key, []) + [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        values = self.hmap[key]

        l = 0
        r = len(values) - 1
        curr = -1
        while l <= r:
            mid = (l + r) // 2
            v, t = values[mid]
            if t > timestamp:
                r = mid - 1
            elif t < timestamp:
                curr = mid
                l = mid + 1
            else:
                return v

        return values[curr][0] if curr > -1 else ""


        
