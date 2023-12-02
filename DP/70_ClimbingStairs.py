class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        a, b = 2, 3
        for i in range(4, n + 1):
            cur = a + b
            a, b = b, cur
        return cur