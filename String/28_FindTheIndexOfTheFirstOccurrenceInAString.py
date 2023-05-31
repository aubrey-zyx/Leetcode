class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if m < n:
            return -1
        for i in range(m - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1


# KMP
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)

        # create "next"
        next = [0]
        k = 0  # longest common prefix and suffix
        for i in range(1, n):
            while k > 0 and needle[k] != needle[i]:
                k = next[k - 1]
            if needle[k] == needle[i]:
                k += 1
            next.append(k)

        # match haystack and needle
        j = 0
        for i in range(m):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == n:
                return i - j + 1
        return -1