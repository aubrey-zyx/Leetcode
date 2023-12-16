class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1] * n

        for i in range(n * 2 - 1):
            while stack and nums[i % n] > nums[stack[-1]]:
                res[stack.pop()] = nums[i % n]
            stack.append(i % n)

        return res