class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for p in points:
            heapq.heappush(max_heap, (-(p[0] ** 2 + p[1] ** 2), p))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [candidate[1] for candidate in max_heap]