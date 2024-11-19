from sortedcontainers import SortedList

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        left_min = nums[0]
        right_nums = SortedList(nums[2:])

        for j in range(1, n - 1):
            if left_min < nums[j]:
                idx = right_nums.bisect_right(left_min)
                if idx < len(right_nums) and right_nums[idx] < nums[j]:
                    return True
            left_min = min(left_min, nums[j])
            right_nums.remove(nums[j + 1])

        return False


# Monotonic stack
class Solution2:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        stack = []
        k = float("-inf")
        for i in range(n - 1, -1, -1):
            if nums[i] < k:
                return True
            while stack and stack[-1] < nums[i]:
                k = max(k, stack.pop())
            stack.append(nums[i])
        return False