class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = []
        count = 0
        for num in nums:
            if num == 0:
                count += 1
            else:
                non_zero.append(num)
        nums[:] = non_zero + [0] * count


# two pointers
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[w] = nums[w], nums[i]
                w += 1