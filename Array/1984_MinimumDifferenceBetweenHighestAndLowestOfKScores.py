class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = float("inf")
        nums.sort()
        for r in range(k - 1, len(nums)):
            l = r - k + 1
            res = min(res, nums[r] - nums[l])
        return res