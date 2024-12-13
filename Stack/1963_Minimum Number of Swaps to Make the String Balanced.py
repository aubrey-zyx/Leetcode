class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        unbalanced = 0
        for c in s:
            if c == "[":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    unbalanced += 1
        return (unbalanced + 1) // 2


# Space-Optimized Stack
class Solution2:
    def minSwaps(self, s: str) -> int:
        unbalanced = 0
        for c in s:
            if c == "[":
                unbalanced += 1
            else:
                if unbalanced:
                    unbalanced -= 1
        return (unbalanced + 1) // 2