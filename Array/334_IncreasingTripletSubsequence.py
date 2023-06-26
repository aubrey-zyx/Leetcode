from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        left_min = [0] * n
        left_min[0] = nums[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i-1], nums[i])
        right_max = [0] * n
        right_max[n-1] = nums[-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], nums[i])
        for i in range(n):
            if left_min[i] < nums[i] < right_max[i]:
                return True
        return False


class Solution2:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        first, second = float('inf'), float('inf')
        for third in nums:
            if third > second:
                return True
            if third <= first:
                first = third
            else:
                second = third
        return False