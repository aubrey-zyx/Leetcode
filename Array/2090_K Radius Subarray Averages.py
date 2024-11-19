class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        if k == 0:
            return nums

        win_size = 2 * k + 1
        if win_size > n:
            return res

        win_sum = sum(nums[:win_size])
        res[k] = win_sum // win_size

        for i in range(win_size, n):
            win_sum = win_sum + nums[i] - nums[i - win_size]
            res[i - k] = win_sum // win_size

        return res