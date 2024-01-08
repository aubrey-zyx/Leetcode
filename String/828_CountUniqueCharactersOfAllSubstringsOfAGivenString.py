class Solution:
    def uniqueLetterString(self, s: str) -> int:
        idx = collections.defaultdict(list)
        for i, c in enumerate(s):
            idx[c].append(i)

        res = 0
        for arr in idx.values():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                res += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return res