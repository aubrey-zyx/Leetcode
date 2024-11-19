class MyHashMap:

    def __init__(self):
        self.key_space = 2069
        self.buckets = [Bucket() for _ in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.key_space
        self.buckets[idx].update(key, value)

    def get(self, key: int) -> int:
        idx = key % self.key_space
        return self.buckets[idx].get(key)

    def remove(self, key: int) -> None:
        idx = key % self.key_space
        self.buckets[idx].remove(key)


class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)