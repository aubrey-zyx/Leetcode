from collections import defaultdict
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
            if cnt[num] > 1:
                return True
        return False


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False