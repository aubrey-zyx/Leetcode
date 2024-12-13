class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length, count = [1] * n, [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_len = max(length)
        res = 0
        for i in range(n):
            if length[i] == max_len:
                res += count[i]
        return res