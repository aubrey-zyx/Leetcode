class Solution:
    def largestVariance(self, s: str) -> int:
        res = 0
        for a in set(s):
            for b in set(s):
                diff, diff_b = 0, float("-inf")
                if a == b:
                    continue
                for ch in s:
                    if ch == a:
                        diff += 1
                        diff_b += 1
                    elif ch == b:
                        diff -= 1
                        diff_b = diff
                        if diff < 0:
                            diff = 0
                    res = max(res, diff_b)
        return res