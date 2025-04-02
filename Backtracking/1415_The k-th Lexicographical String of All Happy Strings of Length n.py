class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        cur = ""
        self.backtrack(n, cur, res)
        if len(res) < k:
            return ""
        return res[k - 1]

    def backtrack(self, n, cur, res):
        if len(cur) == n:
            res.append(cur)
            return
        for c in ['a', 'b', 'c']:
            if len(cur) > 0 and cur[-1] == c:
                continue
            self.backtrack(n, cur + c, res)


# Stop early
class Solution2:
    def getHappyString(self, n: int, k: int) -> str:
        res = ""
        idx = 0

        def backtrack(cur):
            nonlocal res, idx
            if len(cur) == n:
                idx += 1
                if idx == k:
                    res = cur
                return
            for c in ['a', 'b', 'c']:
                if len(cur) > 0 and cur[-1] == c:
                    continue
                backtrack(cur + c)
                if res != "":
                    return

        backtrack("")
        return res