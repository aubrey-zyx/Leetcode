class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = r = 0
        res = 0
        freq = [0] * 3
        n = len(s)

        for r in range(n):
            freq[ord(s[r]) - ord('a')] += 1
            while self._has_all_chars(freq):
                res += n - r
                freq[ord(s[l]) - ord('a')] -= 1
                l += 1

        return res

    def _has_all_chars(self, freq):
        return all(f > 0 for f in freq)