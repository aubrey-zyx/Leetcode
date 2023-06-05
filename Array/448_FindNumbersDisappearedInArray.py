from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_set = set(nums)
        ans = []
        for i in range(1, n + 1):
            if i not in nums_set:
                ans.append(i)
        return ans


class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                p = nums[i]
                nums[i], nums[p - 1] = nums[p - 1], nums[i]
        return [i + 1 for i, num in enumerate(nums) if num - 1 != i]


class Solution3:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            x = (num - 1) % n
            nums[x] += n
        return [i + 1 for i, num in enumerate(nums) if num <= n]