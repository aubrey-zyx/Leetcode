class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        queue = deque()
        for i in range(n):
            if queue and queue[0] < i - k + 1:
                queue.popleft()
            if queue and nums[i] != nums[i - 1] + 1:
                queue.clear()
            queue.append(i)
            if i >= k - 1:
                if len(queue) == k:
                    res.append(nums[i])
                else:
                    res.append(-1)
        return res


# Optimized Via Counter
class Solution2:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        n = len(nums)
        res = [-1] * (n - k + 1)
        consecutive = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                consecutive += 1
            else:
                consecutive = 1
            if consecutive >= k:
                res[i - k + 1] = nums[i]
        return res