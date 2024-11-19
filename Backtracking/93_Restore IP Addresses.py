class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res

        def backtrack(i, dots, cur):
            nonlocal res
            if dots == 4 and i == len(s):
                res.append(cur[:-1])
                return
            if dots > 4:
                return

            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j + 1]) <= 255 and (s[i] != "0" or i == j):
                    backtrack(j + 1, dots + 1, cur + s[i:j + 1] + ".")

        backtrack(0, 0, "")
        return res