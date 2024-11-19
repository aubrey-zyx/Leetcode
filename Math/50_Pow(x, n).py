class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        res = 1
        power = abs(n)
        while power > 0:
            if power % 2 == 1:
                res *= x
                power -= 1
            x *= x
            power //= 2
        return res if n > 0 else 1.0 / res


class Solution2:
    def myPow(self, x: float, n: int) -> float:
        def binaryExp(x, n):
            if n == 0:
                return 1
            if n % 2 == 1:
                return x * binaryExp(x * x, (n - 1) // 2)
            else:
                return binaryExp(x * x, n // 2)

        return binaryExp(x, n) if n >= 0 else 1.0 / binaryExp(x, -n)