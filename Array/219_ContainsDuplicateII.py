from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for i, num in enumerate(nums):
            if num in pos and i - pos[num] <= k:
                return True
            pos[num] = i
        return False


# sliding window
class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        win = set()
        for i, num in enumerate(nums):
            if i > k:
                win.remove(nums[i - k - 1])
            if num in win:
                return True
            win.add(num)
        return False