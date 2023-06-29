from typing import List


class Solution:    # binary search
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 1, n - 1
        while left < right:
            mid = (left + right) // 2
            cnt = sum(num <= mid for num in nums)
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid
        return left


class Solution2:     # fast & slow pointers
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:     # "While slow != fast" will not work because initially they are both set to 0
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # reset slow to 0 and let two pointers move at the same pace, they will meet at the duplicate number (the entrance to the loop)
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow