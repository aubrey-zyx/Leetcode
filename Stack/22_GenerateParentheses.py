class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add a closing parenthesis if close < open

        stack = []
        ans = []

        def backtrack(open, close):
            if open == close == n:
                ans.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()

        backtrack(0, 0)
        return ans


class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                dfs(left + 1, right, s + "(")

            if right < left:
                dfs(left, right + 1, s + ")")

        res = []
        dfs(0, 0, "")
        return res