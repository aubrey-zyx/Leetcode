class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        m = len(part)

        for c in s:
            stack.append(c)
            if len(stack) >= m and self.check_match(stack, part, m):
                for _ in range(m):
                    stack.pop()

        return "".join(stack)

    def check_match(self, stack, part, m):
        return "".join(stack[-m:]) == part