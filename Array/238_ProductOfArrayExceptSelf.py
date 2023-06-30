from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product, right_product = [1] * n, [1] * n
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]
        return [left_product[i] * right_product[i] for i in range(n)]


class Solution2:    # optimize space complexity to O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        right_product = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]
        return ans