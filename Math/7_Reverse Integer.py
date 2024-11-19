class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        res, x = 0, abs(x)
        INT_MAX = 2 ** 31 - 1
        while x:
            x, mod = divmod(x, 10)
            if sign == 1:
                if (res > INT_MAX // 10) or (res == INT_MAX // 10 and mod > 7):
                    return 0
            elif sign == -1:
                if (res > INT_MAX // 10) or (res == INT_MAX // 10 and mod > 8):
                    return 0
            res = res * 10 + mod
        return sign * res