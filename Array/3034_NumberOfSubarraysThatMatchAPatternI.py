class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def compare(a, b):
            if a == b:
                return 0
            else:
                return 1 if a < b else -1

        res = 0
        for i in range(len(nums) - len(pattern)):
            match = True
            for k, pattern_val in enumerate(pattern):
                if compare(nums[i + k], nums[i + k + 1]) != pattern_val:
                    match = False
                    break
            if match:
                res += 1
        return res