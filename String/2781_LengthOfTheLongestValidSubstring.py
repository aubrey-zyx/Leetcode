class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        res = 0
        l = 0
        for r in range(len(word)):
            for i in range(r, max(r - 10, l - 1), -1):
                if word[i: r + 1] in forbidden_set:
                    l = i + 1
                    break
            res = max(res, r - l + 1)
        return res