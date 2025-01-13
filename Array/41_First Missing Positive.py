class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [False] * (n + 1)
        for num in nums:
            if 0 < num <= n:
                seen[num] = True
        for i in range(1, n + 1):
            if not seen[i]:
                return i
        return n + 1


# In-place. O(1) auxiliary space
class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        contains_one = False

        for i in range(n):
            if nums[i] == 1:
                contains_one = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        if not contains_one:
            return 1

        for i in range(n):
            value = abs(nums[i])
            if value == n:
                nums[0] = -abs(nums[0])
            else:
                nums[value] = -abs(nums[value])

        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n
        return n + 1


# Cycle Sort
class Solution3:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1