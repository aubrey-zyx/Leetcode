class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ht = defaultdict(list)
        for i, c in enumerate(s):
            ht[c].append(i)
        res = 0
        for c in ht:
            if len(ht[c]) < 2:
                continue
            between = set()
            for i in range(ht[c][0] + 1, ht[c][-1]):
                between.add(s[i])
            res += len(between)
        return res