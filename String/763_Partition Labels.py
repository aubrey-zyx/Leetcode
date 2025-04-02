class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i, c in enumerate(s):
            last[ord(c) - ord('a')] = i

        res = []
        start = end = 0

        for i, c in enumerate(s):
            end = max(end, last[ord(c) - ord('a')])
            if i == end:
                res.append(i - start + 1)
                start = i + 1

        return res