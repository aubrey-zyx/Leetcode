class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i, num in enumerate(nums):
                if not used[i]:
                    path.append(num)
                    used[i] = True
                    backtrack(path)
                    path.pop()
                    used[i] = False

        backtrack([])
        return res


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(x):
            if x == len(nums) - 1:
                res.append(nums.copy())
                return
            for i in range(x, len(nums)):
                nums[x], nums[i] = nums[i], nums[x]
                dfs(x + 1)
                nums[x], nums[i] = nums[i], nums[x]

        dfs(0)
        return res


class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)

        return res