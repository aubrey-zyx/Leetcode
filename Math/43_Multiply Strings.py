class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                prod = int(num1[i]) * int(num2[j])
                total = prod + res[i + j + 1]
                res[i + j + 1] = total % 10
                res[i + j] += total // 10

        product = "".join(map(str, res)).lstrip("0")
        return product if product else "0"