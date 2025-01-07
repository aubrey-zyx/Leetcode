class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        s = "".join([chr(n + 48) for n in nums])
        res = 0
        n = len(s)
        for i in range(1, n - 1):
            if s[i:].startswith(s[:i]):
                res += n - 2 * i
                for j in range(i + 1, 2 * i):
                    if s[j:].startswith(s[i:j]):
                        res += 1
            else:
                for j in range(i + 1, n):
                    if s[j:].startswith(s[i:j]):
                        res += 1
        return res