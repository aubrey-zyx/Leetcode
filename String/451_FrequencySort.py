import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = collections.Counter(s)
        d_order = sorted(frequency.items(), key=lambda x:x[1], reverse=True)
        res = ""
        for i in range(len(d_order)):
            res += d_order[i][0] * d_order[i][1]
        return res