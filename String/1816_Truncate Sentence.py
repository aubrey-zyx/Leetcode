class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        i = 0
        while i < len(s):
            if s[i] == " ":
                k -= 1
                if k == 0:
                    return s[:i]
            i += 1
        return s