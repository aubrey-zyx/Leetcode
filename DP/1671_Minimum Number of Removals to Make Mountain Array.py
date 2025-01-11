# DP
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lis_dp, lds_dp = [1] * n, [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis_dp[i] = max(lis_dp[i], lis_dp[j] + 1)

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    lds_dp[i] = max(lds_dp[i], lds_dp[j] + 1)

        res = float("inf")
        for i in range(n):
            if lis_dp[i] > 1 and lds_dp[i] > 1:
                res = min(res, n - lis_dp[i] - lds_dp[i] + 1)
        return res


# Binary Search
class Solution2:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lis_len = self.get_lis_Length(nums)
        lds_len = self.get_lis_Length(nums[::-1])
        lds_len.reverse()
        res = float("inf")
        for i in range(n):
            if lis_len[i] > 1 and lds_len[i] > 1:
                res = min(res, n - lis_len[i] - lds_len[i] + 1)
        return res

    def get_lis_Length(self, nums):
        n = len(nums)
        lis_len = [1] * n
        lis = []
        for i, num in enumerate(nums):
            if len(lis) == 0 or num > lis[-1]:
                lis.append(num)
            else:
                idx = self.binary_search_left(lis, num)
                lis[idx] = num
            lis_len[i] = len(lis)
        return lis_len

    def binary_search_left(self, lis, target):
        l, r = 0, len(lis)
        while l < r:
            m = l + (r - l) // 2
            if target > lis[m]:
                l = m + 1
            else:
                r = m
        return l