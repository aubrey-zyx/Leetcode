class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = j = 1
        while j < n:
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i