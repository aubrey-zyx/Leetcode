class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    # Solution 1: sorting
    def top(self, K: int) -> int:
        values = list(self.scores.values())
        values.sort(reverse=True)
        return sum(values[:K])

    # Solution 2: heap
    def top2(self, K: int) -> int:
        heap = []
        for val in self.scores.values():
            heapq.heappush(heap, val)
            if len(heap) > K:
                heapq.heappop(heap)
        return sum(heap[:K])

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)