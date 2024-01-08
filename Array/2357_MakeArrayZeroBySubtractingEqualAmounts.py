class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                x = nums[i]
                for j in range(i, len(nums)):
                    nums[j] -= x
                res += 1
        return res


class Solution2:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - {0})