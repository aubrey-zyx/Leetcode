class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        win_len = sum(nums)
        ones = nums[0]
        max_ones = 0
        end = 0
        for start in range(len(nums)):
            if start > 0:
                ones -= nums[start - 1]
            while end - start + 1 < win_len:
                end += 1
                ones += nums[end % len(nums)]
            max_ones = max(max_ones, ones)
        return win_len - max_ones