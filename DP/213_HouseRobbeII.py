class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_within_range(nums):
            first, second = 0, 0
            for num in nums:
                first, second = second, max(first + num, second)
            return second

        return max(nums[0], rob_within_range(nums[:-1]), rob_within_range(nums[1:]))