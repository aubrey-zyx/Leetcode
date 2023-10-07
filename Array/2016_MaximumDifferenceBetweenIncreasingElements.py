class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        minimum = nums[0]
        for num in nums:
            if num > minimum:
                ans = max(ans, num - minimum)
            else:
                minimum = num
        return ans