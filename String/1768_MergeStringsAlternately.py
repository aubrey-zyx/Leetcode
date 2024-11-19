class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        i = j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged += word1[i]
                i += 1
            if j < len(word2):
                merged += word2[j]
                j += 1
        return merged


class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        m, n = len(word1), len(word2)
        for i in range(min(m, n)):
            res += word1[i]
            res += word2[i]
        if m > n:
            res += word1[i + 1:]
        elif m < n:
            res += word2[i + 1:]
        return res