class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            if len(sub) == 0 or sub[-1] < num:
                sub.append(num)
            else:
                idx = bisect_left(sub, num)  # Find the index of the first element >= num
                sub[idx] = num
        return len(sub)