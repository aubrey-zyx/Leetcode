class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if m < n:
            return -1
        for i in range(m - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for start in range(m - n + 1):
            for i in range(n):
                if haystack[start + i] != needle[i]:
                    break
                if i == n - 1:
                    return start
        return -1


# KMP
class Solution3:
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


# Rabin-Karp Algorithm - Rolling Hash
class Solution4:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if n < m:
            return -1

        BASE = 26
        MOD = 1_000_000_033
        MAX_WEIGHT = 1
        for _ in range(m):
            MAX_WEIGHT = (MAX_WEIGHT * BASE) % MOD

        def get_hash(string):
            res = 0
            factor = 1
            for i in range(m - 1, -1, -1):
                res += ((ord(string[i]) - 97) * factor) % MOD
                factor = (factor * BASE) % MOD
            return res % MOD

        hash_needle = get_hash(needle)

        for start in range(n - m + 1):
            if start == 0:
                hash_hay = get_hash(haystack)
            else:
                hash_hay = (
                                   (hash_hay * BASE) % MOD
                                   - ((ord(haystack[start - 1]) - 97) * MAX_WEIGHT) % MOD
                                   + (ord(haystack[start + m - 1]) - 97)
                                   + MOD
                           ) % MOD

            if hash_needle == hash_hay:
                for i in range(m):
                    if needle[i] != haystack[start + i]:
                        break
                if i == m - 1:
                    return start

        return -1