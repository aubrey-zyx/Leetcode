class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        res = [-1] * len(queries)
        base = 10 ** ((intLength - 1) // 2)
        for i, q in enumerate(queries):
            if q <= 9 * base:
                s = str(base + q - 1)
                s += s[-2::-1] if intLength % 2 else s[::-1]
                res[i] = int(s)
        return res