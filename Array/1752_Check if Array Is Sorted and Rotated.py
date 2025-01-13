class Solution:
    def check(self, nums: List[int]) -> bool:
        down = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                down += 1
            if down > 1:
                return False
        return nums[-1] <= nums[0] or down == 0