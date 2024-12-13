class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        order = 0
        for i in range(n - 1):
            if order == 0 and nums[i] != nums[i + 1]:
                order = 1 if nums[i] < nums[i + 1] else -1
            if (order == 1 and nums[i] > nums[i + 1]) or (order == -1 and nums[i] < nums[i + 1]):
                return False
        return True


class Solution2:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increasing = False
            if nums[i] < nums[i + 1]:
                decreasing = False
        return increasing or decreasing