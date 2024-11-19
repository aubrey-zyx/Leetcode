class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    res += 1
        res += len(stack)
        return res


class Solution2:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        open = 0
        for c in s:
            if c == "(":
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    res += 1
        return res + open