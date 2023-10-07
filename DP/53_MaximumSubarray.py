class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        pre = 0
        for i in range(len(nums)):
            pre = max(pre + nums[i], nums[i])
            ans = max(ans, pre)
        return ans