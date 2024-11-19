class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if idx >= len(candidates) or total > target:
                return
            for i in range(idx, len(candidates)):
                dfs(i, cur + [candidates[i]], total + candidates[i])

        dfs(0, [], 0)
        return res