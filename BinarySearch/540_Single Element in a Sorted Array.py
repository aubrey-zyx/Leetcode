class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            halves_even = (r - m) % 2 == 0
            if nums[m + 1] == nums[m]:
                if halves_even:
                    l = m + 2
                else:
                    r = m - 1
            elif nums[m - 1] == nums[m]:
                if halves_even:
                    r = m - 2
                else:
                    l = m + 1
            else:
                return nums[m]
        return nums[l]


class Solution2:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if m % 2 == 1:
                m -= 1
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                r = m
        return nums[l]