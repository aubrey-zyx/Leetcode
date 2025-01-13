class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ht = {}
        cur_sum = 0
        res = 0

        for i in range(k):
            cur_sum += nums[i]
            ht[nums[i]] = i
        if len(ht) == k:
            res = cur_sum

        for r in range(k, len(nums)):
            cur_sum += nums[r] - nums[r - k]
            ht[nums[r]] = r
            if ht[nums[r - k]] == r - k:
                del ht[nums[r - k]]
            if len(ht) == k:
                res = max(res, cur_sum)
        return res