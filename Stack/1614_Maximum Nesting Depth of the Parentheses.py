class Solution:
    def maxDepth(self, s: str) -> int:
        open = 0
        max_depth = 0
        for c in s:
            if c == "(":
                open += 1
                max_depth = max(max_depth, open)
            elif c == ")":
                open -= 1
        return max_depth