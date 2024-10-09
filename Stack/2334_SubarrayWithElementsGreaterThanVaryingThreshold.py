class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)

        # The nearest smaller element on the left side
        left, stack = [-1] * n, []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] >= num:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        # The nearest smaller element on the right side
        right, stack = [n] * n, []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        for num, l, r in zip(nums, left, right):
            k = r - l - 1
            if num > threshold // k:
                return k
        return -1