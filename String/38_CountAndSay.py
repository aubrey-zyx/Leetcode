class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n-1)
        res = ""
        i = 0
        for j, ch in enumerate(prev):
            if ch != prev[i]:
                res += str(j-i) + prev[i]
                i = j
        res += str(len(prev) - i) + prev[-1]
        return res