class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        res = 0
        total = 0
        ht = {0: -1}
        for i, num in enumerate(nums):
            total += num
            if total - k in ht:
                res = max(res, i - ht[total - k])
            if total not in ht:
                ht[total] = i
        return res