class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def reverse(start, end):
            nums[start: end + 1] = nums[start: end + 1][::-1]

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        tmp = nums.copy()
        for i in range(n):
            tmp[(i + k) % n] = nums[i]
        nums[:] = tmp
