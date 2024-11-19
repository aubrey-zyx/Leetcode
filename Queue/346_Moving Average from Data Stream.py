class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.total = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.count += 1
        self.total += val
        if self.count > self.size:
            self.total -= self.queue.popleft()
        return self.total / min(self.size, self.count)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)