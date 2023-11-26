class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in ht:
                return [ht[diff], i]
            ht[num] = i