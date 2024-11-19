class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        count = 1
        arr = list(s)
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1] and count == 1:
                res += 1
                arr[i] = arr[i - 1]
            count = 1 - count
        return res


class Solution2:
    def minChanges(self, s: str) -> int:
        res = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                res += 1
        return res