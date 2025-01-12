class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_cnt, t_cnt = Counter(s), Counter(t)
        res = 0
        for c in set(t_cnt.keys()).union(set(s_cnt.keys())):
            if t_cnt[c] > s_cnt[c]:
                res += t_cnt[c] - s_cnt[c]
        return res


class Solution2:
    def minSteps(self, s: str, t: str) -> int:
        s_cnt = Counter(s)
        res = 0
        for c in t:
            if s_cnt[c] > 0:
                s_cnt[c] -= 1
            else:
                res += 1
        return res