class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            # subsets that include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            # subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res