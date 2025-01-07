class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = Counter(s)
        freq_t = Counter(t)
        return True if freq_s == freq_t else False


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
        for c in t:
            cnt[c] -= 1
        for freq in cnt.values():
            if freq != 0:
                return False
        return True