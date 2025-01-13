class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        seen = set()
        res = set()
        for i in range(n - 10 + 1):
            cur = s[i: i + 10]
            if cur in seen:
                res.add(cur)
            seen.add(cur)
        return list(res)


# Rolling Hash
class Solution2:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        L = 10
        if n <= L:
            return []

        ht = {"A": 0, "C": 1, "G": 2, "T": 3}
        nums = [ht[c] for c in s]

        h = 0
        base = 4
        seen, res = set(), set()
        for i in range(n - L + 1):
            if i != 0:
                h = h * base - nums[i - 1] * pow(base, L) + nums[i + L - 1]
            else:
                for j in range(L):
                    h = h * base + nums[j]
            if h in seen:
                res.add(s[i: i + L])
            seen.add(h)
        return list(res)