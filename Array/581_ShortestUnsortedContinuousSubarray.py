from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # Locate initial left and right borders that break monotonic increase
        i, j = 0, n - 1
        while i < j and nums[i] <= nums[i + 1]:
            i += 1
        while i < j and nums[j] >= nums[j - 1]:
            j -= 1
        if i == j:
            return 0

        # Update left and right borders
        mini, maxi = min(nums[i:j + 1]), max(nums[i:j + 1])
        while i > -1:
            if i == 0:
                break
            else:
                if mini >= nums[i - 1]:
                    break
                i -= 1
                mini = min(mini, nums[i])
        while j < n:
            if j == n - 1:
                break
            else:
                if maxi <= nums[j + 1]:
                    break
                j += 1
                maxi = max(maxi, nums[j])

        return j - i + 1


class Solution2:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1
        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]
            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]
        return 0 if right == -1 else right - left + 1


class Solution3:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        nums_sorted = sorted(nums)
        i, j = 0, n - 1
        while i < j and (nums[i] == nums_sorted[i] or nums[j] == nums_sorted[j]):
            if nums[i] == nums_sorted[i]:
                i += 1
            if nums[j] == nums_sorted[j]:
                j -= 1
        return j - i + 1 if i < j else 0