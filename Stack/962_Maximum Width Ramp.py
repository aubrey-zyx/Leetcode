# Sorting
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        indices = [i for i in range(n)]
        indices.sort(key=lambda i: (nums[i], i))
        min_idx = n
        res = 0
        for i in indices:
            res = max(res, i - min_idx)
            min_idx = min(min_idx, i)
        return res


# Monotonic stack
class Solution2:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []

        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        res = 0
        for i in range(n - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                res = max(res, i - stack[-1])
                stack.pop()
        return res