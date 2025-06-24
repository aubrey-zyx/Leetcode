class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = [(-nums[i], i) for i in range(k)]
        heapq.heapify(h)
        res = [-h[0][0]]
        for r in range(k, len(nums)):
            heapq.heappush(h, (-nums[r], r))
            while h[0][1] <= r - k:
                heapq.heappop(h)
            res.append(-h[0][0])
        return res


# Monotonically decreasing queue
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        l = r = 0

        for r in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[r]:
                queue.pop()
            queue.append(r)

            if queue[0] < l:
                queue.popleft()

            if r >= k - 1:
                res.append(nums[queue[0]])
                l += 1

        return res


# Same as 2
class Solution3:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()

        for i in range(k):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        res.append(nums[queue[0]])

        for i in range(k, len(nums)):
            if queue and queue[0] == i - k:
                queue.popleft()
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            res.append(nums[queue[0]])

        return res