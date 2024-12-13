class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        mod = 10 ** 9 + 7
        for left in range(n):
            right = bisect.bisect_right(nums, target - nums[left]) - 1
            if right >= left:
                res += pow(2, right - left, mod)
        return res % mod