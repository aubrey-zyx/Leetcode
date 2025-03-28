class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, path, total):
            if total == target:
                res.append(path.copy())
                return
            if i >= len(candidates) or total > target:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                dfs(j + 1, path + [candidates[j]], total + candidates[j])

        dfs(0, [], 0)
        return res


class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, path, total):
            if total == target:
                res.append(path.copy())
                return
            if i == len(candidates) or total > target:
                return
            path.append(candidates[i])
            dfs(i + 1, path, total + candidates[i])
            path.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, path, total)

        dfs(0, [], 0)
        return res