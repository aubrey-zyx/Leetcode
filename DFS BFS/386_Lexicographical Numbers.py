class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(num, limit):
            nonlocal res
            if num > limit:
                return
            res.append(num)
            for next_digit in range(10):
                next_num = num * 10 + next_digit
                if next_num <= limit:
                    dfs(next_num, limit)
                else:
                    break

        for start in range(1, 10):
            dfs(start, n)
        return res


# Iterative
class Solution2:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        num = 1
        for _ in range(n):
            res.append(num)
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num >= n:
                    num //= 10
                num += 1
        return res