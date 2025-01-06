class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        heap = []
        n = len(nums)
        marked = [False] * n

        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))

        while heap:
            num, i = heapq.heappop(heap)
            if not marked[i]:
                score += num
                marked[i] = True
                if i > 0:
                    marked[i - 1] = True
                if i < n - 1:
                    marked[i + 1] = True

        return score


class Solution2:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        custom = [(num, i) for i, num in enumerate(nums)]
        custom.sort()
        n = len(nums)
        marked = [False] * n

        for num, i in custom:
            if not marked[i]:
                score += num
                marked[i] = True
                if i > 0:
                    marked[i - 1] = True
                if i < n - 1:
                    marked[i + 1] = True

        return score