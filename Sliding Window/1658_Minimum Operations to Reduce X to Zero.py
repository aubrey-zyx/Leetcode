class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        n = len(nums)
        l = cur = 0
        max_len = -1
        for r in range(n):
            cur += nums[r]
            while cur > total - x and l <= r:
                cur -= nums[l]
                l += 1
            if cur == total - x:
                max_len = max(max_len, r - l + 1)
        return n - max_len if max_len != -1 else -1