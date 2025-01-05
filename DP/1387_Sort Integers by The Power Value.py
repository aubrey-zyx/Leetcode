class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}

        def get_power(x):
            if x in memo:
                return memo[x]
            if x == 1:
                return 0
            if x % 2 == 0:
                memo[x] = 1 + get_power(x // 2)
            else:
                memo[x] = 1 + get_power(3 * x + 1)
            return memo[x]

        powers = [(x, get_power(x)) for x in range(lo, hi + 1)]
        powers.sort(key=lambda x: (x[1], x[0]))
        return powers[k - 1][0]