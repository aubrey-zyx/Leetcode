class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                cur = num
                seq_len = 1
                while cur + 1 in nums_set:
                    seq_len += 1
                    cur += 1
                ans = max(ans, seq_len)
        return ans