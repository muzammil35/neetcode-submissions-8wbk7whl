class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []

        self.keys[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""

        arr = self.keys[key]

        l = 0
        r = len(arr) - 1
        result = ""

        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid][0] <= timestamp:
                result = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return result

        
