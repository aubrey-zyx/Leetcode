class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        i = j = 2
        while j < n:
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        w = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                count = 1
            else:
                count += 1
                if count > 2:
                    continue
            nums[w] = nums[i]
            w += 1
        return w