class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_mp = defaultdict(int)
        for i, c in enumerate(order):
            order_mp[c] = i + 1
        return "".join(sorted(s, key=lambda x: order_mp[x]))


class Solution2:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        res = []
        for ch in order:
            if ch in freq:
                res.extend([ch] * freq[ch])
                freq[ch] = 0
        for ch, f in freq.items():
            if f > 0:
                res.extend([ch] * f)
        return "".join(res)