class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n) - sum(rolls)
        if total < n or total > 6 * n:
            return []
        avg, mod = divmod(total, n)
        res = [avg] * n
        for i in range(mod):
            res[i] += 1
        return res