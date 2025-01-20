class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        m = n - 1
        j = 0
        for i in range(64):
            if ((res >> i) & 1) == 0:
                if ((m >> j) & 1) != 0:
                    res |= (1 << i)
                j += 1
        return res