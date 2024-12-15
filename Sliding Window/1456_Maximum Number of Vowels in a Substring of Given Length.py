class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        cur = 0
        for r, c in enumerate(s):
            if c in "aeiou":
                cur += 1
            if r >= k and s[r - k] in "aeiou":
                cur -= 1
            res = max(res, cur)
        return res