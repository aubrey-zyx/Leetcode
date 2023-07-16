class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        w = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[w] = nums[w], nums[i]
                w += 1
        for i in range(w, n):
            if nums[i] == 1:
                nums[i], nums[w] = nums[w], nums[i]
                w += 1


class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left, right, i = 0, n - 1, 0
        while i <= right:
            while i <= right and nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            i += 1