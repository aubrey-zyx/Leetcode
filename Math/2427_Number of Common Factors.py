class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        m = min(a, b)
        res = 0
        for i in range(1, m + 1):
            if a % i == 0 and b % i == 0:
                res += 1
        return res