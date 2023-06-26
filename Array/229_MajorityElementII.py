import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = collections.Counter(nums)
        ans = []
        for key, value in cnt.items():
            if value > n // 3:
                ans.append(key)
        return ans