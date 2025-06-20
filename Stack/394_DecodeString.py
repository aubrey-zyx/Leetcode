# Stack
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == "[":
                stack.append([multi, res])
                res, multi = "", 0
            elif c == "]":
                cur_multi, prev_res = stack.pop()
                res = prev_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res


# Recursion
class Solution2:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if "0" <= s[i] <= "9":
                    multi = multi * 10 + int(s[i])
                elif s[i] == "[":
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == "]":
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s, 0)


# Recursion 2
class Solution3:
    def decodeString(self, s: str) -> str:
        self.i = 0

        def dfs(s):
            res, k = "", 0
            while self.i < len(s):
                c = s[self.i]
                if "0" <= c <= "9":
                    k = k * 10 + int(c)
                elif c == "[":
                    self.i += 1
                    res += k * dfs(s)
                    k = 0
                elif c == "]":
                    return res
                else:
                    res += c
                self.i += 1
            return res

        return dfs(s)