class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(word)
        for c in set(word):
            cnt[c] -= 1
            if cnt[c] == 0:
                del cnt[c]
            if len(set(cnt.values())) == 1:
                return True
            cnt[c] += 1
        return False