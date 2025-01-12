# Two Pointers
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.count_pairs_with_upper_bound(nums, upper + 1) - self.count_pairs_with_upper_bound(nums, lower)

    # Count the number of pairs with sum less than "upper"
    def count_pairs_with_upper_bound(self, nums, upper):
        l, r = 0, len(nums) - 1
        res = 0
        while l < r:
            total = nums[l] + nums[r]
            if total < upper:
                res += r - l
                l += 1
            else:
                r -= 1
        return res


# Binary Search
class Solution2:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n):
            high = self.binary_search(nums, i + 1, n - 1, upper + 1 - nums[i])
            low = self.binary_search(nums, i + 1, n - 1, lower - nums[i])
            res += high - low
        return res

    def binary_search(self, nums, l, r, target):
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
        return l