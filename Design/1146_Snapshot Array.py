class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.history = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.history[index][-1][0] == self.id:
            self.history[index][-1][1] = val
        else:
            self.history[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_idx = bisect.bisect_right(self.history[index], snap_id, key=lambda x: x[0])
        return self.history[index][snap_idx - 1][1]

    # ----- bisect_right implementation -----
    def get2(self, index: int, snap_id: int) -> int:
        records = self.history[index]
        l, r, res = 0, len(records) - 1, 0
        while l <= r:
            m = (l + r) // 2
            if records[m][0] <= snap_id:
                res = m
                l = m + 1
            else:
                r = m - 1
        return records[res][1]

    def get3(self, index: int, snap_id: int) -> int:
        records = self.history[index]
        l, r = 0, len(records)
        while l < r:
            m = (l + r) // 2
            if records[m][0] <= snap_id:
                l = m + 1
            else:
                r = m
        return records[l - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)