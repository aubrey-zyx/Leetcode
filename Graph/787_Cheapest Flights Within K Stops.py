# BFS
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))

        queue = deque([(src, 0)])
        costs = [float("inf")] * n
        while k >= 0 and queue:
            for _ in range(len(queue)):
                node, cost = queue.popleft()
                for nei, price in adj[node]:
                    if cost + price < costs[nei]:
                        costs[nei] = cost + price
                        queue.append((nei, costs[nei]))
            k -= 1

        return costs[dst] if costs[dst] != float("inf") else -1


# Dijkstra
class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visited = {}
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))
        hp = [(0, 0, src)]
        while hp:
            cost, stops, node = heapq.heappop(hp)
            if node == dst and stops <= k + 1:
                return cost
            if node not in visited or visited[node] > stops:
                visited[node] = stops
                for nei, price in adj[node]:
                    heapq.heappush(hp, (cost + price, stops + 1, nei))
        return -1