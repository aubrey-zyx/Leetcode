class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(i, path):
            if i == len(nums):
                if len(path) >= 2:
                    res.add(tuple(path))
                return
            if not path or path[-1] <= nums[i]:
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
            backtrack(i + 1, path)

        backtrack(0, [])
        return [list(seq) for seq in res]