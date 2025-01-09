class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, path):
            res.append(path.copy())
            for i in range(i, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return res


# Iterative
class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]
        return res


# Bit Manipulation
class Solution4:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(1 << n):
            subset = [nums[j] for j in range(n) if i & (1 << j)]
            res.append(subset)
        return res


# Bit
class Solution5:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(2 ** n, 2 ** (n + 1)):
            bitmask = bin(i)[3:]
            subset = [nums[j] for j in range(n) if bitmask[j] == "1"]
            res.append(subset)
        return res