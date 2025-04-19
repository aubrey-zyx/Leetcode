class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1

        pref_sum = 0
        for i in range(n):
            pref_sum += diff[i]
            if nums[i] > pref_sum:
                return False
        return True