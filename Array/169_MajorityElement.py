import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        return cnt.most_common(1)[0][0]


# Boyer–Moore majority vote algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


# Boyer-Moore Vote Algorithm
class Solution2:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = candidate2 = None
        count1 = count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # validation
        count1 = nums.count(candidate1)
        count2 = nums.count(candidate2)
        n = len(nums)
        res = []
        if count1 > n // 3:
            res.append(candidate1)
        if count2 > n // 3:
            res.append(candidate2)

        return res