class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        pre = 0
        for i in range(len(nums)):
            pre = max(pre + nums[i], nums[i])
            ans = max(ans, pre)
        return ans


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res