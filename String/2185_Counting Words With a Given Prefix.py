class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        def has_prefix(word, pref):
            if len(word) < len(pref):
                return False
            i = 0
            while i < len(pref):
                if word[i] != pref[i]:
                    return False
                i += 1
            return True


        count = 0
        for word in words:
            if has_prefix(word, pref):
                count += 1
        return count


class Solution2:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(word.startswith(pref) for word in words)