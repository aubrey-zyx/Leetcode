class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0
        costs = []
        for i in range(len(s)):
            costs.append(abs(ord(s[i]) - ord(t[i])))
        l = 0
        cur_sum = 0
        for r in range(len(costs)):
            cur_sum += costs[r]
            while cur_sum > maxCost:
                cur_sum -= costs[l]
                l += 1
            res = max(res, r - l + 1)
        return res