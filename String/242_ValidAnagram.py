from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = Counter(s)
        freq_t = Counter(t)
        return True if freq_s == freq_t else False