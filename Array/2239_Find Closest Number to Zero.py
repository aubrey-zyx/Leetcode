class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_diff = float("inf")
        res = nums[0]
        for num in nums:
            if abs(num) < min_diff:
                min_diff = abs(num)
                res = num
            elif abs(num) == min_diff:
                res = max(res, num)
        return res