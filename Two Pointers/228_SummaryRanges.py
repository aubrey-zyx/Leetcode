from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ans = []
        i = 0
        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
            if j != i:
                ans.append(str(nums[i]) + "->" + str(nums[j]))
                i = j + 1
            else:
                ans.append(str(nums[i]))
                i += 1
        return ans